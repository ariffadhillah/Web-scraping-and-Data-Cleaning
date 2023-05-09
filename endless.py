import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

fields = ['Parttype (category)', 'Parttype URL (category)', 'Make', 'Make URL', 'Model', 'Model URL', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'endless.csv'



processed_urls = set()
categoryProduct = []

# Page Brake pads
pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

r = requests.get(pageBrakepads, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
listCarsName = []
listImportedCar = []
data = []



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
                print(pageCarlist)
                
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
brake_caliper = baseurl + '/products/brake_caliper/index.html'


r = requests.get(brake_caliper, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listCarsName = []
listImportedCar = []
data = []
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

    test = soup.find('div', class_='maintitle_pc_box2')
    print(test.text.strip())

