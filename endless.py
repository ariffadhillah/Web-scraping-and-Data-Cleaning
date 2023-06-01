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

r = requests.get(pageBrakepads, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')
listCarsName = []
listImportedCar = []

brakepad_search_whole = soup.find('div', id='brakepad_search_whole')

# 
carList = brakepad_search_whole.find('div', id='right_menu_box')
for linkcars in carList.find_all('a', href=True):
    listCarsName.append(linkcars['href'])
for carName in listCarsName:
    urlcar = requests.get(carName, headers=headers, verify=False)
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
                r = requests.get(pageCarlist, headers=headers, verify=False)
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
                            year = row.find_all('td')
                            engine = row.find_all('td')
                            type_ = row.find_all('td')
                            PartNumberFront = row.find_all('td')
                            PartNumberRear = row.find_all('td')[13:]
                            if PartNumberFront and PartNumberRear:
                                PartNumber = PartNumberFront[4].text.strip() +' '+ PartNumberRear[0].text.strip()
                            else:
                                PartNumber = ""                            

                            endless = {
                                'Parttype (category)': parttype_category,
                                'Parttype URL (category)': parttype_category_url,
                                'Make': url.split('/')[-2].replace('-', ' ').title(),
                                'Make URL': carName,
                                'Model': model.text.strip(),
                                'Model URL': pageCarlist,
                                'Series': '',
                                'Year': year[1].text.strip(),
                                'Engine cc': engine[2].text.strip() if len(engine) >= 3 else '',
                                'Type': type_[3].text.strip() if len(type_) >= 4 else '',
                                'PartNumber': PartNumber.replace(' ', '\n'),
                            }
                            if year and PartNumber and engine:
                                data.append(endless)
                                print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])
                                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                                    writer.writeheader()
                                    for item in data:
                                        writer.writerow(item)



urllistimport1 = [
    'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_AUDI.html',
    'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_MERCEDES.html'
]

data = []

for urlimportlist in urllistimport1:
    r = requests.get(urlimportlist, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    iframesimport = soup.find_all('iframe')
    for iframeimport in iframesimport:
        src = iframeimport['src']
        iframeimport_content = requests.get(src).content
        iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
        tablesimport = iframeimport_soup.find_all('table')

        for tablemodelimport in tablesimport:
            rowsmodelimport = tablemodelimport.find_all('tr')[2]
            modelimport = rowsmodelimport.find_all('td')[1]

        for table in tablesimport:
            rows = table.find_all('tr')[5:]
            for row in rows:
                removetext = [
                    '※1 EIP132かEIP149のいずれかになります。形状図にてご確認ください。',
                    '※2 EIP159、EIP162、EIP165、EIP232の価格は他の品番と異なりますのでご注意ください.'
                ]
                if any(text in td.text.strip() for td in row for text in removetext):
                    continue
                # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
                if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                    continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
                try:
                    td_elementsmodel = row.find_all('td')
                    if len(td_elementsmodel) == 12:
                        model = td_elementsmodel[1].text.strip()
                    else:
                        model = ''
                except:
                    model = ''
                try:
                    td_elementsseries = row.find_all('td')
                    if len(td_elementsseries) == 12:
                        series = td_elementsseries[5].text.strip()
                    else:
                        series = ''
                except:
                    series = ''
                try:
                    td_elementsyears = row.find_all('td')
                    if len(td_elementsyears) == 12:
                        years = td_elementsyears[4].text.strip()
                    else:
                        years = ''
                except:
                    years = ''

                partNumberFront = row.find_all('td')
                partNumberRear = row.find_all('td')[9:]
                if partNumberFront and partNumberRear:
                    partNumber = partNumberFront[6].text.strip() + ' ' + partNumberRear[0].text.strip()
                else:
                    partNumber = ""

                endless = {
                    'Parttype (category)': 'ブレーキパッド',
                    'Parttype URL (category)': 'https://www.endless-sport.co.jp/products/brake_pad/index.html',
                    'Make': modelimport.text.strip(),
                    'Make URL': urlimportlist,
                    'Model': model,
                    'Model URL': '',
                    "Series": series,
                    'Year': years,
                    'Engine cc': '',
                    'Type': '',
                    'PartNumber': partNumber.replace(' ', '\n'),
                }
                if model and partNumber:
                    data.append(endless)
                    print('Saving', endless['Make'], endless['Model'], endless['Type'], endless['Year'],endless['Series'], endless['PartNumber'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)



urllistimport1 = ['https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_ALFAROMEO.html' ,'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_PEUGEOT.html' 
,'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_BMWMINI.html', 'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_FIAT.html','https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_LOTUS.html','https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_RENAULT.html']

for urlimportlist in urllistimport1:
    r = requests.get(urlimportlist, headers=headers ,verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    make = soup.find('div', class_='maintitle_pc_box2').text.strip()

    divmodel = soup.find_all('div', class_='slidebox2')
    for div in divmodel:
        modelbraek_line = div.text.strip().replace('＋ ', '') 
                
        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')

            for table in tables:
                rows = table.find_all('tr')[3:]
                for row in rows:
                    removetext = ['test']
                    if any(text in td.text.strip() for td in row for text in removetext):
                        continue
                    if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                        continue                   
                    try:
                        td_elementsyears = row.find_all('td')
                        if len(td_elementsyears) == 15:
                            years = td_elementsyears[3].text.strip()
                        else:
                            years = ''           
                    except:
                        years = ''

                    try:
                        td_elementsSeries = row.find_all('td')
                        if len(td_elementsSeries) == 15:
                            modelSeries = td_elementsSeries[4].text.strip()
                        else:
                            modelSeries = ''           
                    except:
                        modelSeries = ''

                    partNumberFront = row.find_all('td')
                    partNumberRear = row.find_all('td')[10:]
                    if partNumberFront and partNumberRear:
                        partNumber = partNumberFront[5].text.strip() +' '+ partNumberRear[0].text.strip()
                    else:
                        partNumber = ""
                    
                    endless = {
                        'Parttype (category)': 'ブレーキパッド',
                        'Parttype URL (category)': 'https://www.endless-sport.co.jp/products/products_index.html',
                        'Make':make ,
                        'Make URL': urlimportlist,
                        'Model': modelbraek_line,
                        'Model URL': urlimportlist,
                        "Series": modelSeries,
                        'Year':  years,
                        'Engine cc':'' ,
                        'Type': '',
                        'PartNumber': partNumber.replace(' ', '\n'),
                    }
                    if years and  partNumber:
                        data.append(endless)
                        print('Saving', endless['Make URL'], endless['Make'], endless['Model'],endless['Type'], endless['Year'],  endless['Series'],  endless['PartNumber'])
                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)


urllistimport1 = ['https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_BMW.html']

for urlimportlist in urllistimport1:
    r = requests.get(urlimportlist, headers=headers ,verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    make = soup.find('div', class_='maintitle_pc_box2').text.strip()

iframesimport = soup.find_all('iframe')
for iframeimport in iframesimport:
    src = iframeimport['src']
    iframeimport_content = requests.get(src).content
    iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
    tablesimport = iframeimport_soup.find_all('table')     
        
    for tablemodelimport in tablesimport:
        rowsmodelimport = tablemodelimport.find_all('tr')[2]
        modelimport =  rowsmodelimport.find_all('td')[1]
    for table in tablesimport:
        rows = table.find_all('tr')[6:]
        for row in rows:
            removetext = ['フロント']
            if any(text in td.text.strip() for td in row for text in removetext):
                continue
            if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                continue     
                          
            
            td_elementsmodel = row.find_all('td')
            try:
                if len(td_elementsmodel) == 21:
                    model = td_elementsmodel[1].text.strip()   
                elif len(td_elementsmodel) == 21:
                    continue
                else:
                    model = td_elementsmodel[1].text.strip()                                                
            except:
                None   

            try:
                td_elementsyears = row.find_all('td')
                if len(td_elementsyears) == 21:
                    years = td_elementsyears[3].text.strip()
                elif len(td_elementsyears) == 21:
                    years = td_elementsyears[3].text.strip()
                else:
                    years = ''
            except:
                years = ''

            try:
                td_elementsSeries = row.find_all('td')
                if len(td_elementsSeries) == 21:
                    modelSeries = td_elementsSeries[4].text.strip()
                else:
                    modelSeries = ''
            except:
                modelSeries = ''

            try:
                td_elementsType = row.find_all('td')
                if len(td_elementsType) == 21:
                    modelType = td_elementsType[2].text.strip()
                elif len(td_elementsType) == 20:
                    modelType = td_elementsType[1].text.strip()
                else:
                    modelType = ''
            except:
                modelType = ''

            try:
                td_elementspartNumberFront = row.find_all('td')
                if len(td_elementspartNumberFront) == 21:
                    modelpartNumberFront = td_elementspartNumberFront[5].text.strip()
                elif len(td_elementspartNumberFront) == 20:
                    modelpartNumberFront = td_elementspartNumberFront[4].text.strip()
                else:
                    modelpartNumberFront = ''
            except:
                modelpartNumberFront = ''

            try:
                td_elementspartNumberRear = row.find_all('td')
                if len(td_elementspartNumberRear) == 21:
                    modelpartNumberRear = td_elementspartNumberRear[13].text.strip()
                elif len(td_elementspartNumberRear) == 20:
                    modelpartNumberRear = td_elementspartNumberRear[12].text.strip()
                else:
                    modelpartNumberRear = ''
            except:
                modelpartNumberRear = ''

            if modelpartNumberFront and modelpartNumberRear:
                partNumber = modelpartNumberFront + ' ' + modelpartNumberRear
            else:
                partNumber = ""

            if partNumber and modelSeries:
                endless = {
                    'Parttype (category)': 'ブレーキパッド',
                    'Parttype URL (category)':'https://www.endless-sport.co.jp/products/brake_pad/index.html',
                    'Make':make,
                    'Make URL': urlimportlist,
                    'Model': model,
                    'Model URL': urlimportlist,
                    "Series":modelSeries,
                    'Year':  years,
                    'Engine cc':'' ,
                    'Type': '',
                    'PartNumber': partNumber.replace(' ', '\n'),
                }
                if modelType and years and model:
                    data.append(endless)
                    print('Saving', endless['Parttype (category)'], endless['Make URL'], endless['Make'], endless['Model'], endless['Type'], endless['Year'],  endless['Series'],  endless['PartNumber'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)


urllistimport1 = ['https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_PORSCHE.html']

for urlimportlist in urllistimport1:
    r = requests.get(urlimportlist, headers=headers ,verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    make = soup.find('div', class_='maintitle_pc_box2').text.strip()

iframesimport = soup.find_all('iframe')
for iframeimport in iframesimport:
    src = iframeimport['src']
    iframeimport_content = requests.get(src).content
    iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
    tablesimport = iframeimport_soup.find_all('table')     
        
    for tablemodelimport in tablesimport:
        rowsmodelimport = tablemodelimport.find_all('tr')[2]
        modelimport =  rowsmodelimport.find_all('td')[1]
    for table in tablesimport:
        rows = table.find_all('tr')[4:]
        for row in rows:
            removetext = ['フロント']
            if any(text in td.text.strip() for td in row for text in removetext):
                continue
            if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                continue   
            
            try:
                td_elementsModel = row.find_all('td')
                if len(td_elementsModel) == 26:
                    model = td_elementsModel[1].text.strip()
                else:
                    model = ''           
            except:
                model = ''

            try:
                td_elementsyears = row.find_all('td')
                if len(td_elementsyears) == 26:
                    years = td_elementsyears[4].text.strip()
                else:
                    years = ''           
            except:
                years = ''

            try:
                td_elementsSeries = row.find_all('td')
                if len(td_elementsSeries) == 26:
                    modelSeries = td_elementsSeries[5].text.strip()
                else:
                    modelSeries = ''           
            except:
                modelSeries = ''

            try:
                td_elementsengine = row.find_all('td')
                if len(td_elementsengine) == 26:
                    engine = td_elementsengine[2].text.strip()
                else:
                    engine = ''           
            except:
                engine = '' 

            try:
                td_elementspartNumberFront = row.find_all('td')
                if len(td_elementspartNumberFront) == 26:
                    modelpartNumberFront = td_elementspartNumberFront[6].text.strip()
                else:
                    modelpartNumberFront = ''           
            except:
                modelpartNumberFront = ''

            try:
                td_elementspartNumberRear = row.find_all('td')
                if len(td_elementspartNumberRear) == 26:
                    modelpartNumberRear = td_elementspartNumberRear[16].text.strip()
                else:
                    modelpartNumberRear = ''           
            except:
                modelpartNumberRear = ''

            if modelpartNumberFront and modelpartNumberRear:
                partNumber = modelpartNumberFront +' '+ modelpartNumberRear
            else:
                partNumber = ""

            endless = {
                'Parttype (category)': 'ブレーキパッド',
                'Parttype URL (category)':'https://www.endless-sport.co.jp/products/brake_pad/index.html' ,
                'Make':make,
                'Make URL': urlimportlist,
                'Model': model,
                'Model URL': urlimportlist,
                "Series":modelSeries,
                'Year':  years,
                'Engine cc': '',
                'Type': '',
                'PartNumber': partNumber.replace(' ', '\n'),
            }
            if years and partNumber and model:
                data.append(endless)
                print('Saving', endless['Parttype (category)'], endless['Make URL'], endless['Make'], endless['Model'], endless['Type'], endless['Year'],  endless['Series'],  endless['PartNumber'])
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)


urllistimport1 = [
    'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_VOLVO.html',
    'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_VOLKSWAGEN.html'
]


for urlimportlist in urllistimport1:
    r = requests.get(urlimportlist, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    make = soup.find('div', class_='maintitle_pc_box2').text.strip()

    iframesimport = soup.find_all('iframe')
    for iframeimport in iframesimport:
        src = iframeimport['src']
        iframeimport_content = requests.get(src).content
        iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
        tablesimport = iframeimport_soup.find_all('table')

        for tablemodelimport in tablesimport:
            rowsmodelimport = tablemodelimport.find_all('tr')[2]
            modelimport = rowsmodelimport.find_all('td')[1]

        for table in tablesimport:
            rows = table.find_all('tr')[4:]
            for row in rows:
                removetext = ['フロント']
                if any(text in td.text.strip() for td in row for text in removetext):
                    continue
                if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                    continue
                try:
                    td_elementsmodel = row.find_all('td')
                    if len(td_elementsmodel) == 16:
                        model = td_elementsmodel[1].text.strip()
                    else:
                        model = ''
                except:
                    model = ''
                try:
                    td_elementsyears = row.find_all('td')
                    if len(td_elementsyears) == 16:
                        years = td_elementsyears[4].text.strip()
                    else:
                        years = ''
                except:
                    years = ''

                try:
                    td_elementsSeries = row.find_all('td')
                    if len(td_elementsSeries) == 16:
                        modelSeries = td_elementsSeries[5].text.strip()
                    else:
                        modelSeries = ''
                except:
                    modelSeries = ''

                try:
                    td_elementsType = row.find_all('td')
                    if len(td_elementsType) == 16:
                        modelType = td_elementsType[2].text.strip()
                    else:
                        modelType = ''
                except:
                    modelType = ''

                try:
                    td_elementspartNumberFront = row.find_all('td')
                    if len(td_elementspartNumberFront) == 16:
                        modelpartNumberFront = td_elementspartNumberFront[6].text.strip()
                    else:
                        modelpartNumberFront = ''
                except:
                    modelpartNumberFront = ''

                try:
                    td_elementspartNumberRear = row.find_all('td')
                    if len(td_elementspartNumberRear) == 16:
                        modelpartNumberRear = td_elementspartNumberRear[11].text.strip()
                    else:
                        modelpartNumberRear = ''
                except:
                    modelpartNumberRear = ''

                if modelpartNumberFront and modelpartNumberRear:
                    partNumber = modelpartNumberFront + ' ' + modelpartNumberRear
                else:
                    partNumber = ""

                endless = {
                    'Parttype (category)': 'ブレーキパッド',
                    'Parttype URL (category)': 'https://www.endless-sport.co.jp/products/brake_pad/index.html',
                    'Make': make,
                    'Make URL': urlimportlist,
                    'Model': model,
                    'Model URL': urlimportlist,
                    "Series": modelSeries,
                    'Year': years,
                    'Engine cc': '',
                    'Type': '',
                    'PartNumber': partNumber.replace(' ', '\n'),
                }
                if years:
                    data.append(endless)
                    print('Saving', endless['Parttype (category)'], endless['Make'],endless['Model'], endless['Type'], endless['Year'], endless['Series'], endless['PartNumber'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)


urllistimport1 = ['https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_FERRARI.html']

for urlimportlist in urllistimport1:
    r = requests.get(urlimportlist, headers=headers ,verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    make = soup.find('div', class_='maintitle_pc_box2').text.strip()

iframesimport = soup.find_all('iframe')
for iframeimport in iframesimport:
    src = iframeimport['src']
    iframeimport_content = requests.get(src).content
    iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
    tablesimport = iframeimport_soup.find_all('table')     
        
    for tablemodelimport in tablesimport:
        rowsmodelimport = tablemodelimport.find_all('tr')[2]
        modelimport =  rowsmodelimport.find_all('td')[1]
    for table in tablesimport:
        rows = table.find_all('tr')[4:]
        for row in rows:
            removetext = ['フロント']
            if any(text in td.text.strip() for td in row for text in removetext):
                continue
            if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                continue                   
            try:
                td_elementsmodel = row.find_all('td')
                if len(td_elementsmodel) == 8:
                    model = td_elementsmodel[1].text.strip()
                else:
                    model = ''           
            except:
                years = ''
            try:
                td_elementsyears = row.find_all('td')
                if len(td_elementsyears) == 8:
                    years = td_elementsyears[4].text.strip()
                else:
                    years = ''           
            except:
                years = ''

            try:
                td_elementsSeries = row.find_all('td')
                if len(td_elementsSeries) == 8:
                    modelSeries = td_elementsSeries[5].text.strip()
                else:
                    modelSeries = ''           
            except:
                modelSeries = ''

            try:
                td_elementsType = row.find_all('td')
                if len(td_elementsType) == 8:
                    modelType = td_elementsType[2].text.strip()
                else:
                    modelType = ''           
            except:
                modelType = ''


            partNumberFront = row.find_all('td')
            partNumberRear = row.find_all('td')[7:]
            if partNumberFront and partNumberRear:
                partNumber = partNumberFront[6].text.strip() +' '+ partNumberRear[0].text.strip()
            else:
                partNumber = ""
            endless = {
                'Parttype (category)': 'ブレーキパッド',
                'Parttype URL (category)':'https://www.endless-sport.co.jp/products/products_index.html' ,
                'Make':make,
                'Make URL': urlimportlist,
                'Model': model,
                'Model URL': '',
                "Series":modelSeries,
                'Year':  years,
                'Engine cc':'' ,
                'Type': modelType,
                'PartNumber': partNumber.replace(' ', '\n'),
            }
            if modelType and  partNumber:
                data.append(endless)
                print('Saving', endless['Parttype (category)'], endless['Make URL'], endless['Make'], endless['Model'], endless['Type'], endless['Year'],  endless['Series'],  endless['PartNumber'])
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)

# time.sleep(.1)                
# #product imported 
# importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
# for linkcarsimported in importedCar.find_all('a', href=True):
#     urlimported = linkcarsimported['href'].replace('https://', 'https://www.')
#     if urlimported not in processed_urls:
#         listImportedCar.append(urlimported)
#         processed_urls.add(urlimported)

# for pageCarListImport in listImportedCar:
#     time.sleep(.1)
#     r = requests.get(pageCarListImport, headers=headers, verify=False)
#     soup = BeautifulSoup(r.content, 'lxml')    

#     # testdiv = soup.find('div', id='maintitle_pc')
#     # print(testdiv)

#     cautionContents = soup.find('div', {'class': 'caution_contents'}) or soup.find('div', {'id': 'caution_contents'})
#     if cautionContents:
#         caution_links = cautionContents.find_all('a')
#         category = caution_links[1]
#         parttype_category_url = category['href']
#         parttype_category = category.text.strip()


#     iframesimport = soup.find_all('iframe')
#     for iframeimport in iframesimport:
#         src = iframeimport['src']
#         iframeimport_content = requests.get(src).content
#         iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#         tablesimport = iframeimport_soup.find_all('table')
#         # print(tables)
#         for tableMake in tablesimport:
#             rowsMake = tableMake.find_all('tr')[1]
#             makeimport =  rowsMake.find_all('td')[1]
        
#         for tablemodelimport in tablesimport:
#             rowsmodelimport = tablemodelimport.find_all('tr')[2]
#             modelimport =  rowsmodelimport.find_all('td')[1]
            

#         for table in tablesimport:
#             rows = table.find_all('tr')[5:]
#             for row in rows:
#                 # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
#                 if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#                     continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
#                 year = row.find_all('td')
#                 engine = row.find_all('td')
#                 type_ = row.find_all('td')
#                 PartNumberFront = row.find_all('td')
#                 PartNumberRear = row.find_all('td')[10:]
#                 if PartNumberFront and PartNumberRear:
#                     PartNumber = PartNumberFront[5].text.strip() +' '+ PartNumberRear[0].text.strip()
#                 else:
#                     PartNumber = ""
                
#                 endless = {
#                     'Parttype (category)': parttype_category,
#                     'Parttype URL (category)': parttype_category_url,
#                     'Make': makeimport.text.strip(),
#                     'Make URL': pageBrakepads,
#                     'Model': modelimport.text.strip(),
#                     'Model URL': pageCarListImport,
#                     "Series": ' ',
#                     'Year': year[3].text.strip().replace('～', ' ～ '),
#                     'Engine cc': ' ',
#                     'Type': type_[4].text.strip(),
#                     'PartNumber': PartNumber.replace(' ', '\n'),
#                 }
#                 if year and PartNumber:
#                     data.append(endless)
#                     print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])                   
#                     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#                         writer = csv.DictWriter(csvfile, fieldnames=fields)
#                         writer.writeheader()
#                         for item in data:
#                             writer.writerow(item)



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
    r = requests.get(crasListBrakeCaliper, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    
    listCarsBrakeCaliper = soup.find_all('div', id='maker_icons')
    
    for listMake in listCarsBrakeCaliper:
        for linkMake in listMake.find_all('a', href=True):
            linkModel.append(linkMake['href'])

for linkMake in linkModel:
    r = requests.get(linkMake, headers=headers, verify=False)
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
                            print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])                    
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

r = requests.get(brake_rotor, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

# tekigou_icon

listbrakerotor = soup.find_all('div', class_='tekigou_icon')[1:]

listbrakerotorlinks = []

for itembrakerotor in listbrakerotor:
    for namecarslistbrakerotor in itembrakerotor.find_all('a', href=True):
        # print(namecarslistbrakerotor['href']) 
         listbrakerotorlinks.append(namecarslistbrakerotor['href']) 

for pagelistbrakerotor in listbrakerotorlinks:
    r = requests.get(pagelistbrakerotor, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    try:
        makebrakerotor = soup.find('div', 'maintitle_pc_box2').text.strip()
    except:
        makebrakerotor = ''
        
    divmodel = soup.find_all('div', class_='slidebox2')[1:]
        
    for div in divmodel:
        modelbrakerotor = div.text.strip().replace('＋ ', '')  
            
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
                        'Parttype URL (category)': brake_rotor,
                        'Make': makebrakerotor,
                        'Make URL': pagelistbrakerotor,
                        'Model':  modelbrakerotor,
                        'Model URL': pagelistbrakerotor,
                        'Year':  '',
                        'Series': model,
                        'Engine cc': '',
                        'Type': '',
                        'PartNumber':partNumberbrakerotor,
                    }
                    if model and partNumberbrakerotor:
                        data.append(endless)
                        print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])
                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)


brake_line = baseurl + '/products/brake_line/index.html'

r = requests.get(brake_line, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

listbrake_line = soup.find('select', onchange='location.href=value;')

itembrake_line = listbrake_line.find_all('option')[:10]
linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]
# listbrake_linelinks.append(linknameCarsbrake_line)
# print(linknameCarsbrake_line)

for listbrake_linelinks in linknameCarsbrake_line:
    r = requests.get(listbrake_linelinks, headers=headers, verify=False)
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
                    
                    endless = {
                        'Parttype (category)': 'ブレーキライン',
                        'Parttype URL (category)': brake_line,
                        'Make': makebraek_line,
                        'Make URL': listbrake_linelinks,
                        'Model':  modelbraek_line,
                        'Model URL': listbrake_linelinks,
                        'Year':  '',
                        'Series': '',
                        'Engine cc': '',
                        'Type': typebraek_line,
                        'PartNumber':partNumberbraek_line,
                    }
                    if typebraek_line and partNumberbraek_line:
                        data.append(endless)
                        print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])
                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)


brake_line = baseurl + '/products/brake_line/index.html'

r = requests.get(brake_line, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

listbrake_line = soup.find('select', onchange='location.href=value;')

itembrake_line = listbrake_line.find_all('option')[10:]
linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]
# listbrake_linelinks.append(linknameCarsbrake_line)
# print(linknameCarsbrake_line)

for listbrake_linelinks in linknameCarsbrake_line:
    r = requests.get(listbrake_linelinks, headers=headers,verify=False )
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
                        'Model URL': listbrake_linelinks,
                        'Year':  year,
                        'Series': series,
                        'Engine cc': '',
                        'Type': typebraek_line,
                        'PartNumber':partNumberbraek_line,
                    }
                    data.append(endless)
                    if  typebraek_line and partNumberbraek_line and year and series:
                        print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])
                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)


suspensionUlr = baseurl + '/products/suspension/index_functionxplus.html'
r = requests.get(suspensionUlr, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

listsuspension = soup.find('select', onchange='location.href=value;')

itembrake_line = listsuspension.find_all('option')[:2]
linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]

for listsuspensionlinks in linknameCarsbrake_line:
    r = requests.get(listsuspensionlinks, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    makesuspension = soup.find('div', 'maintitle_pc_box2').text.strip()
    iframes = soup.find_all('iframe')
    for iframe in iframes:
        src = iframe['src']
        iframe_content = requests.get(src).content
        iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
        tables = iframe_soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')[7:]
            for row in rows:
                td_elements = row.find_all('td')
                removetext = ['test']
                if any(text in td.text.strip() for td in td_elements for text in removetext):
                    continue
                try:
                    if len(td_elements) == 14:
                        CarModel = td_elements[1].text.strip()
                    else:
                        CarModel = ''
                except:
                    CarModel = ''

                try:
                    if len(td_elements) == 14:
                        CarSeries = td_elements[2].text.strip()
                    else:
                        CarSeries = ''
                except:
                    CarSeries = ''

                try:
                    if len(td_elements) == 14:
                        partNumber = td_elements[8].text.strip()
                    else:
                        partNumber = ''
                except:
                    partNumber = ''

                endless = {
                    'Parttype (category)': 'サスペンション',
                    'Parttype URL (category)': suspensionUlr,
                    'Make': makesuspension,
                    'Make URL': listsuspensionlinks,
                    'Model':  CarModel,
                    'Model URL': '',
                    'Year':  '',
                    'Series': CarSeries,
                    'Engine cc': '',
                    'Type': '',
                    'PartNumber': partNumber,
                }

                if CarModel and CarSeries and partNumber:
                    data.append(endless)
                    print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)


itembrake_line = listsuspension.find_all('option')[2:]
linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]

for listsuspensionlinks in linknameCarsbrake_line:
    r = requests.get(listsuspensionlinks, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    makesuspension = soup.find('div', 'maintitle_pc_box2').text.strip()

    divmodel = soup.find_all('div', class_='slidebox2')[1:]        
    for div in divmodel:
        engine_cc = div.text.strip()
        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')[7:]
                for row in rows:
                    td_elements = row.find_all('td')
                    removetext = ['test']
                    if any(text in td.text.strip() for td in td_elements for text in removetext):
                        continue
                    try:
                        if len(td_elements) == 15:
                            CarsMake = td_elements[1].text.strip()
                        else:
                            CarsMake = ''
                    except:
                        CarsMake = ''
                    
                    try:
                        if len(td_elements) == 15:
                            CarsMakeModel = td_elements[2].text.strip()
                        else:
                            CarsMakeModel = ''
                    except:
                        CarsMakeModel = ''                    
                    try:
                        if len(td_elements) == 15:
                            CarsMakeModelSeries = td_elements[3].text.strip()
                        else:
                            CarsMakeModelSeries = ''
                    except:
                        CarsMakeModelSeries = ''                
                    try:
                        if len(td_elements) == 15:
                            CarsPartNumber = td_elements[9].text.strip()
                        else:
                            CarsPartNumber = ''
                    except:
                        CarsPartNumber = ''

                    endless = {
                        'Parttype (category)': 'サスペンション',
                        'Parttype URL (category)': suspensionUlr,
                        'Make': makesuspension,
                        'Make URL': listsuspensionlinks,
                        'Model': CarsMakeModel,
                        'Model URL': '',
                        'Year':  '',
                        'Series': CarsMakeModelSeries,
                        'Engine cc':  '',
                        'Type': CarsMake,
                        'PartNumber': CarsPartNumber,
                    }

                    if CarsMake and CarsMakeModel and CarsMakeModelSeries and CarsPartNumber:
                        data.append(endless)
                        print('Saving', endless['Make'], endless['Make URL'], endless['Model'],  endless['PartNumber'])
                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)
