import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_ALFAROMEO.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

fields = ['Parttype (category)', 'Parttype URL (category)', 'Make', 'Make URL', 'Model', 'Model URL', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'Example.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
data = []

cautionContents = soup.find('div', {'class': 'caution_contents'}) or soup.find('div', {'id': 'caution_contents'})
if cautionContents:
    caution_links = cautionContents.find_all('a')
    category = caution_links[1]
    parttype_category_url = category['href']
    parttype_category = category.text.strip()

# menhapus <tr> dengan ketinggian tertentu seperti contoh ini tinggi 'height: 149px'
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
                
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)


hreflink = "https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_VOLVO.html"
r = requests.get(hreflink, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

cautionContents = soup.find('div', {'class': 'caution_contents'}) or soup.find('div', {'id': 'caution_contents'})
if cautionContents:
    caution_links = cautionContents.find_all('a')
    category = caution_links[1]
    parttype_category_url = category['href']
    parttype_category = category.text.strip()

# menhapus <tr> dengan ketinggian tertentu seperti contoh ini tinggi 'height: 149px'
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
                
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)