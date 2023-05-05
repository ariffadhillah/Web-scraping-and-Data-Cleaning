import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

processed_urls = set()
categoryProduct = []
listImportedCar = []

pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

r = requests.get(pageBrakepads, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
listCarsName = []
data = []

brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
for linkcarsimported in importedCar.find_all('a', href=True):
    urlimported = linkcarsimported['href'].replace('https://', 'https://www.')
    if urlimported not in processed_urls:
        listImportedCar.append(urlimported)
        processed_urls.add(urlimported)

for pageCarListImport in listImportedCar:
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
                        'Make URL': '',
                        'Model': modelimport.text.strip(),
                        'Model URL': '',
                        'Year': year[3].text.strip().replace('～', ' ～ '),
                        'Engine cc': ' ',
                        'Type': type_[4].text.strip(),
                        'PartNumber': PartNumber.replace(' ', '\n'),
                    }
                    data.append(endless)
                    print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
                    
                    # with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    #     writer = csv.DictWriter(csvfile, fieldnames=fields)
                    #     writer.writeheader()
                    #     for item in data:
                    #         writer.writerow(item)
