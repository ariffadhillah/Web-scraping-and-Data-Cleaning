import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}


fields = ['Parttype (category)', 'Parttype URL (category)', 'Make', 'Make URL', 'Model', 'Model URL', 'Series', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'endless.csv'

data = []


processed_urls = set()


categoryProduct = []

# Page Brake pads
pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

r = requests.get(pageBrakepads, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
listCarsName = []
listImportedCar = []



brakepad_search_whole = soup.find('div', id='brakepad_search_whole')

# 
carList = brakepad_search_whole.find('div', id='right_menu_box')
for linkcars in carList.find_all('a', href=True):
    listCarsName.append(linkcars['href'])
for carName in listCarsName:
    urlcar = requests.get(carName, headers=headers)
    soup = BeautifulSoup(urlcar.content, 'lxml')
    # print(carName)
    carNameIcons = soup.find_all('div', id='ewig_pad_whole')
    for itemCarName in carNameIcons:
        for href in itemCarName.find_all('a',  href=True):
            productList = []
            # print(len(href))
            url = href['href']
            if url not in processed_urls:
                productList.append(pageBrakepads.replace('/car_list.html', '/') + url)
                processed_urls.add(url)

            for pageCarlist in productList:
                time.sleep(.1)
                r = requests.get(pageCarlist, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')
                # print(pageCarlist)
                
                caution_contents = soup.find('div', {'class': 'caution_contents'}) or soup.find('div', {'id': 'caution_contents'})
                if caution_contents:
                    caution_links = caution_contents.find_all('a')
                    category = caution_links[1]
                    parttype_category_url = category['href']
                    parttype_category = category.text.strip()

                # # menhapus <tr> dengan ketinggian tertentu seperti contoh ini tinggi 'height: 149px'
                iframes = soup.find_all('iframe')
                for iframe in iframes:
                    src = iframe['src']
                    iframe_content = requests.get(src).content
                    iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
                    tables = iframe_soup.find_all('table')

                    for tablemodel in tables:
                        rowsmodel = tablemodel.find_all('tr')[2]
                        model =  rowsmodel.find_all('td')[1]

                    for table in tables:
                        rows = table.find_all('tr')[5:]
                        for row in rows:
                            # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
                            # if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                            #     continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
                            year = row.find_all('td')
                            engine = row.find_all('td')
                            type_ = row.find_all('td')
                            PartNumberFront = row.find_all('td')
                            PartNumberRear = row.find_all('td')[13:]
                            if PartNumberFront and PartNumberRear:
                                PartNumber = PartNumberFront[4].text.strip() +' '+ PartNumberRear[0].text.strip()
                            else:
                                PartNumber = ""                            

                            if year and engine and type_ and PartNumber and model and parttype_category_url and parttype_category:
                                endless = {
                                    'Parttype (category)': parttype_category,
                                    'Parttype URL (category)': parttype_category_url,
                                    'Make': url.split('/')[-2].replace('-', ' ').title(),
                                    'Make URL': carName,
                                    'Model': model.text.strip(),
                                    'Model URL': pageCarlist,
                                    'Series': '',
                                    'Year': year[1].text.strip(),
                                    'Engine cc': engine[2].text.strip(),
                                    'Type': type_[3].text.strip(),
                                    'PartNumber': PartNumber.replace(' ', '\n'),
                                }
                                data.append(endless)
                                print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])

                                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                                    writer.writeheader()
                                    for item in data:
                                        writer.writerow(item)
time.sleep(.1)                
#product imported 
importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
for linkcarsimported in importedCar.find_all('a', href=True):
    urlimported = linkcarsimported['href'].replace('https://', 'https://www.')
    if urlimported not in processed_urls:
        listImportedCar.append(urlimported)
        processed_urls.add(urlimported)

for pageCarListImport in listImportedCar:
    time.sleep(.1)
    r = requests.get(pageCarListImport, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')    

    # testdiv = soup.find('div', id='maintitle_pc')
    # print(testdiv)

    cautionContents = soup.find('div', {'class': 'caution_contents'}) or soup.find('div', {'id': 'caution_contents'})
    if cautionContents:
        caution_links = cautionContents.find_all('a')
        category = caution_links[1]
        parttype_category_url = category['href']
        parttype_category = category.text.strip()


    iframesimport = soup.find_all('iframe')
    for iframeimport in iframesimport:
        src = iframeimport['src']
        iframeimport_content = requests.get(src).content
        iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
        tablesimport = iframeimport_soup.find_all('table')
        # print(tables)
        for tableMake in tablesimport:
            rowsMake = tableMake.find_all('tr')[1]
            makeimport =  rowsMake.find_all('td')[1]
        
        for tablemodelimport in tablesimport:
            rowsmodelimport = tablemodelimport.find_all('tr')[2]
            modelimport =  rowsmodelimport.find_all('td')[1]
            

        for table in tablesimport:
            rows = table.find_all('tr')[5:]
            for row in rows:
                # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
                if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                    continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
                year = row.find_all('td')
                engine = row.find_all('td')
                type_ = row.find_all('td')
                PartNumberFront = row.find_all('td')
                PartNumberRear = row.find_all('td')[10:]
                if PartNumberFront and PartNumberRear:
                    PartNumber = PartNumberFront[5].text.strip() +' '+ PartNumberRear[0].text.strip()
                else:
                    PartNumber = ""
                
                if year and engine and type_ and PartNumber:
                    endless = {
                        'Parttype (category)': parttype_category,
                        'Parttype URL (category)': parttype_category_url,
                        'Make': makeimport.text.strip(),
                        'Make URL': pageBrakepads,
                        'Model': modelimport.text.strip(),
                        'Model URL': pageCarListImport,
                        "Series": ' ',
                        'Year': year[3].text.strip().replace('～', ' ～ '),
                        'Engine cc': ' ',
                        'Type': type_[4].text.strip(),
                        'PartNumber': PartNumber.replace(' ', '\n'),
                    }
                    data.append(endless)
                    print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])                    
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)



# Page Brake pads
time.sleep(.1) 
brake_caliper = baseurl + '/products/brake_caliper/index.html'
r = requests.get(brake_caliper, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listCarsName = []
listImportedCar = []

list_Brake_caliper = []

links_index2 = []
linkModel = []
leftmenuindex1 = soup.find('div', id='leftmenu_index2')
for urlCarsList in leftmenuindex1.find_all('a', href=True):
    links_index2.append(urlCarsList['href'])

for crasListBrakeCaliper in links_index2:
    r = requests.get(crasListBrakeCaliper, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    listCarsBrakeCaliper = soup.find_all('div', id='maker_icons')
    
    for listMake in listCarsBrakeCaliper:
        for linkMake in listMake.find_all('a', href=True):
            linkModel.append(linkMake['href'])

for linkMake in linkModel:
    r = requests.get(linkMake, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    make = soup.find('div', class_="maintitle_pc_box2").text.strip()
    divmodel = soup.find_all('div', class_='slidebox2')

    for div in divmodel:
        model = div.h1.text.strip()
        # print(model)
        enginecc = div.text.replace(model, '').strip()

        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')

            for table in tables:
                PartNumber = []
                rows = table.find_all('tr')
                for row in rows:
                    if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                        continue
                    td_elements = row.find_all('td')
                    try:
                        type_ = td_elements[1].text.strip()
                        if len(type_) < 0:
                            continue
                        PartNumber = td_elements[6].text.strip()
                        if len(PartNumber) < 10:
                            continue
                        if  type_ and PartNumber:
                            endless = {
                                'Parttype (category)': 'ブレーキキャリパー',
                                'Parttype URL (category)': brake_caliper,
                                'Make': make,
                                'Make URL': crasListBrakeCaliper,
                                'Model': model,
                                'Model URL': linkMake,
                                "Series": '',
                                'Year': '',
                                'Engine cc': enginecc,
                                'Type': type_,
                                'PartNumber': PartNumber,
                            }
                            data.append(endless)
                            print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])                    
                            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.DictWriter(csvfile, fieldnames=fields)
                                writer.writeheader()
                                for item in data:
                                    writer.writerow(item)
                    except:
                        None
                        

# Page Brake pads
time.sleep(.1) 

brake_rotor = baseurl + '/products/brake_rotor/index.html'

r = requests.get(brake_rotor, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# tekigou_icon

listbrakerotor = soup.find_all('div', class_='tekigou_icon')[1:]

listbrakerotorlinks = []

for itembrakerotor in listbrakerotor:
    for namecarslistbrakerotor in itembrakerotor.find_all('a', href=True):
        # print(namecarslistbrakerotor['href']) 
         listbrakerotorlinks.append(namecarslistbrakerotor['href']) 

for pagelistbrakerotor in listbrakerotorlinks:
    r = requests.get(pagelistbrakerotor, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    try:
        makebrakerotor = soup.find('div', 'maintitle_pc_box2').text.strip()
    except:
        makebrakerotor = ''
        
    divmodel = soup.find_all('div', class_='slidebox2')[1:]
        
    for div in divmodel:
        modelbrakerotor = div.text.strip() 
            
        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')

            year = ''       
            model =''
            typebraek_line = ''
            partNumberbraek_line = ''
            series = ''
                    
            for table in tables:
                rows = table.find_all('tr')[4:]
                for row in rows:
                    td_elementsmodel = row.find_all('td')
                    removetext = ['商品名', '1PCSブレーキローター','2PCSブレーキローター','3PCSブレーキローター','¥61,600','補修ブレーキローター','品番','※純正ブレーキローターの寸法をご確認くださいませ。','※ベルハウジング及び固定ピンは純正を再使用してください。（固定用ボルト、ナットは付属します）','※ER154、155のディスクローター補修部品は、純正ブレーキローターの補修用としてはご使用いただけませんのでご注意ください。','※レガシィBE／BHは車種により装着できない場合がございます。車検証情報から適合調査をさせて頂きます。','※ディスク単体での販売となります。ベルハウジング及び固定ピンは純正をご使用ください。','※純正に比べ、厚みが25mmから26.5mmへ変更しております。ブレーキパッドのシムは外してからご使用ください。','※ドリルドタイプのみとなります。','※ベルハウジングはステンレス製でシルバーとなります。色変更はお受けしておりません。','※リアドラム部はスチール製となります。','※ASSYでの販売となります。','※本製品の販売につきましては、エンドレス認定ショップのみとなります。ご購入をご希望される方は、弊社までお問い合わせください。','※1 本製品の販売につきましては、生産を一時終了させていただいております。（詳しくはこちらをご覧くださいませ）','ベルハウジングの色はレーシングアルマイトとなります。色変更に関しては「ベルハウジングオーダーカラー」をご覧くださいませ','※ベルハウジングの色はレーシングアルマイトとなります。色変更に関しては「 ベルハウジングオーダーカラー」をご覧くださいませ']
                    if any(text in td.text.strip() for td in td_elementsmodel for text in removetext):
                        continue
                    try:
                        if len(td_elementsmodel) == 8:
                            model = td_elementsmodel[1].text.strip()   
                        elif len(td_elementsmodel) == 7:
                            continue
                        else:
                            model = td_elementsmodel[1].text.strip()   
                                             
                    except:
                        None                
                   
                    td_elementspartNumber = row.find_all('td')
                    removetext = ['品番']
                    if any(text in td.text.strip() for td in td_elementspartNumber for text in removetext):
                        continue
                    try:
                        if len(td_elementspartNumber) == 8:
                            partNumberbrakerotor = td_elementspartNumber[2].text.strip()   
                        elif len(td_elementspartNumber) == 7:
                            continue
                        else:
                            partNumberbrakerotor = td_elementspartNumber[2].text.strip()   
                                             
                    except:
                        None      
                   
                    endless = {
                        'Parttype (category)': 'ブレーキライン',
                        'Parttype URL (category)': '',
                        'Make': makebrakerotor,
                        'Make URL': '',
                        'Model':  modelbrakerotor,
                        'Model URL': '',
                        'Year':  '',
                        'Series': model,
                        'Engine cc': '',
                        'Type': '',
                        'PartNumber':partNumberbrakerotor,
                    }
                    data.append(endless)
                    print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)



brake_line = baseurl + '/products/brake_line/index.html'

r = requests.get(brake_line, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listbrake_line = soup.find('select', onchange='location.href=value;')

itembrake_line = listbrake_line.find_all('option')[:10]
linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]
# listbrake_linelinks.append(linknameCarsbrake_line)
# print(linknameCarsbrake_line)

for listbrake_linelinks in linknameCarsbrake_line:
    r = requests.get(listbrake_linelinks, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
    divmodel = soup.find_all('div', class_='slidebox2')

    for div in divmodel:
        modelbraek_line = div.text.strip() 
                
        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')
            
            year = ''       
            model =''
            typebraek_line = ''
            partNumberbraek_line = ''
            series = ''
            
            for table in tables:
                rows = table.find_all('tr')[3:]
                for row in rows:
                    try:
                        td_elementspartNumber = row.find_all('td')
                        # Seri
                        if len(td_elementspartNumber) == 15:
                            partNumberbraek_line = td_elementspartNumber[3].text.strip()
                        elif len(td_elementspartNumber) == 14:
                            partNumberbraek_line = td_elementspartNumber[2].text.strip()
                        else:
                            partNumberbraek_line = ' '
                    except:
                        partNumberbraek_line = ''

                    try:                    
                        td_elementstypebraek_line = row.find_all('td')
                        if len(td_elementstypebraek_line) == 15:
                            typebraek_line = td_elementstypebraek_line[2].text.strip()
                        elif len(td_elementstypebraek_line) == 14:
                            typebraek_line = td_elementstypebraek_line[1].text.strip()
                        else:
                            typebraek_line = ''
                    except:
                        typebraek_line = ' '
                    
                    # print(modelbraek_line, typebraek_line, partNumberbraek_line)

                    if typebraek_line and partNumberbraek_line:
                        endless = {
                            'Parttype (category)': 'ブレーキライン',
                            'Parttype URL (category)': '',
                            'Make': makebraek_line,
                            'Make URL': listbrake_linelinks,
                            'Model':  modelbraek_line,
                            'Model URL': '',
                            'Year':  '',
                            'Series': '',
                            'Engine cc': '',
                            'Type': typebraek_line,
                            'PartNumber':partNumberbraek_line,
                        }
                        data.append(endless)
                        print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])
                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)

        





brake_line = baseurl + '/products/brake_line/index.html'

r = requests.get(brake_line, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listbrake_line = soup.find('select', onchange='location.href=value;')

itembrake_line = listbrake_line.find_all('option')[10:]
linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]
# listbrake_linelinks.append(linknameCarsbrake_line)
# print(linknameCarsbrake_line)

for listbrake_linelinks in linknameCarsbrake_line:
    r = requests.get(listbrake_linelinks, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
    divmodel = soup.find_all('div', class_='slidebox2')

    for div in divmodel:
        modelbraek_line = div.text.strip() 
                
        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')
            
            year = ''       
            model =''
            typebraek_line = ''
            partNumberbraek_line = ''
            series = ''
                    
            for table in tables:
                rows = table.find_all('tr')[4:]
                for row in rows:
                    td_elementsmodel = row.find_all('td')
                    try:
                        if len(td_elementsmodel) == 11:
                            model = td_elementsmodel[1].text.strip()                    
                    except:
                        None                
                
                    try:
                        td_elementsyear = row.find_all('td')
                        if len(td_elementsyear) == 11:
                            year = td_elementsyear[3].text.strip()
                        elif len(td_elementsyear) == 10:
                            year = td_elementsyear[2].text.strip()
                        else:
                            year = ' '
                    except:
                        year = ' '
                    
                    try:
                        # Seri
                        td_elementsseries = row.find_all('td')
                        if len(td_elementsseries) == 11:
                            series = td_elementsseries[4].text.strip()
                        elif len(td_elementsseries) == 10:
                            series = td_elementsseries[3].text.strip()
                        else:
                            series = '  '
                    except:
                        series = '  '
                        
                    try:
                        td_elementspartNumber = row.find_all('td')
                        # Seri
                        if len(td_elementspartNumber) == 11:
                            partNumberbraek_line = td_elementspartNumber[5].text.strip()
                        elif len(td_elementspartNumber) == 10:
                            partNumberbraek_line = td_elementspartNumber[4].text.strip()
                        else:
                            partNumberbraek_line = ' '
                    except:
                        partNumberbraek_line = ''

                    try:                    
                        td_elementstypebraek_line = row.find_all('td')
                        if len(td_elementstypebraek_line) == 11:
                            typebraek_line = td_elementstypebraek_line[2].text.strip()
                        elif len(td_elementstypebraek_line) == 10:
                            typebraek_line = td_elementstypebraek_line[1].text.strip()
                        else:
                            typebraek_line = ''
                    except:
                        typebraek_line = ' '

                    endless = {
                        'Parttype (category)': 'ブレーキライン',
                        'Parttype URL (category)': brake_line,
                        'Make': modelbraek_line,
                        'Make URL': listbrake_linelinks,
                        'Model':  model,
                        'Model URL': '',
                        'Year':  year,
                        'Series': series,
                        'Engine cc': '',
                        'Type': typebraek_line,
                        'PartNumber':partNumberbraek_line,
                    }
                    data.append(endless)
                    print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)


