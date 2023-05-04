import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.endless-sport.co.jp/products/brake_pad/carlist/honda/HONDA_Accord.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}
fields = ['Parttype (category)', 'Parttype url (category)', 'Make', 'Make URL', 'Model', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'endless.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
data = []

parttypeCategory = soup.find('div', id='caution_contents')
parttypeCategorylinks = parttypeCategory.find_all('a')
category = parttypeCategorylinks[1]
parttype_category_url = category['href']
parttype_category = category.text.strip()

# menhapus <tr> dengan ketinggian tertentu seperti contoh ini tinggi 'height: 149px'
iframes = soup.find_all('iframe')
for iframe in iframes:
    src = iframe['src']
    iframe_content = requests.get(src).content
    iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
    tables = iframe_soup.find_all('table')
    for tablemodel in tables:
        rowsmodel = tablemodel.find_all('tr')[1]
        print(rowsmodel.find_all('td')[1])
    for table in tables:
        rows = table.find_all('tr')[5:]
        for row in rows:
            # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
            if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
            year = row.find_all('td')
            engine = row.find_all('td')
            type_ = row.find_all('td')
            PartNumberFront = row.find_all('td')
            PartNumberRear = row.find_all('td')[13:]
            if PartNumberFront and PartNumberRear:
                PartNumber = PartNumberFront[4].text.strip() +' '+ PartNumberRear[0].text.strip()
            else:
                PartNumber = ""
            
            if year and engine and type_ and PartNumber:
                endless = {
                    'Parttype (category)': parttype_category,
                    'Parttype url (category)': parttype_category_url,
                    'Make': url.split('/')[-2].replace('-', ' ').title(),
                    'Make URL': '',
                    'Model': '',
                    'Year': year[1].text.strip().replace('～', ' ～ '),
                    'Engine cc': engine[2].text.strip().replace('～', ' ～ '),
                    'Type': type_[3].text.strip(),
                    'PartNumber': PartNumber.replace(' ', '\n'),
                }
                data.append(endless)
                print('Saving',endless['Make'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])

                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)
