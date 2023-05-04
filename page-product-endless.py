# import requests
# from bs4 import BeautifulSoup
# import csv

# url = "https://www.endless-sport.co.jp/products/brake_pad/carlist/toyota/TOYOTA_isis.html"
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# fields = ['Parttype (category)', 'Parttype url (category)', 'Make', 'Make URL', 'Model', 'Year', 'Engine cc', 'Type', 'PartNumber']
# filename = 'endless.csv'

# data = []
# iframe_divs = soup.find_all('div', id='PFBC_all')
# for iframe_div in iframe_divs:
#     iframes = iframe_div.find_all('iframe')
#     for iframe in iframes:
#         src = iframe['src']
#         iframe_content = requests.get(src).content
#         iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#         tables = iframe_soup.find_all('table')
#         for table in tables:
#             rows = table.find_all('tr')[5:]
#             for row in rows:
#                 year = row.find_all('td')
#                 engine = row.find_all('td')
#                 type_ = row.find_all('td')
#                 PartNumberFront = row.find_all('td')
#                 PartNumberRear = row.find_all('td')
#                 if PartNumberFront and PartNumberRear:
#                     PartNumber = PartNumberFront[3].text.strip() + PartNumberRear[11].text.strip()
#                 else:
#                     PartNumber = ""
#                 if year and engine and type_ and PartNumber:
#                     endless = {
#                         'Parttype (category)': '',
#                         'Parttype url (category)': '',
#                         'Make': '',
#                         'Make URL': '',
#                         'Model': '',
#                         'Year': year[0].text.strip(),
#                         'Engine cc': engine[1].text.strip(),
#                         'Type': type_[2].text.strip(),
#                         'PartNumber': PartNumber,
#                     }
#                     data.append(endless)
#                     print('Saving', endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
                    
#                 with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#                     writer = csv.DictWriter(csvfile, fieldnames=fields)
#                     writer.writeheader()
#                     for item in data:
#                         writer.writerow(item)




# import requests
# from bs4 import BeautifulSoup
# import csv

# url = "https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/lexus/LEXUS_IS.html"
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# fields = ['Parttype (category)', 'Parttype url (category)', 'Make', 'Make URL', 'Model', 'Year', 'Engine cc', 'Type', 'PartNumber']
# filename = 'endless.csv'

# data = []

# iframes = soup.find_all('iframe')
# for iframe in iframes:
#     src = iframe['src']
#     iframe_content = requests.get(src).content
#     iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#     tables = iframe_soup.find_all('table')
#     for table in tables:
#         rows = table.find_all('tr')[5:]
#         for row in rows:
#             year = row.find_all('td')
#             engine = row.find_all('td')
#             type_ = row.find_all('td')
#             PartNumberFront = row.find_all('td')
#             PartNumberRear = row.find_all('td')
#             if PartNumberFront and PartNumberRear:
#                 PartNumber = PartNumberFront[4].text.strip() + PartNumberRear[11].text.strip()
#             else:
#                 PartNumber = ""
#             if year and engine and type_ and PartNumber:
#                 endless = {
#                     'Parttype (category)': '',
#                     'Parttype url (category)': '',
#                     'Make': '',
#                     'Make URL': '',
#                     'Model': '',
#                     'Year': year[0].text.strip(),
#                     'Engine cc': engine[1].text.strip(),
#                     'Type': type_[2].text.strip(),
#                     'PartNumber': PartNumber.replace(' ', '\n'),
#                 }
#                 data.append(endless)
#                 print('Saving', endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
                    
# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)


import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.endless-sport.co.jp/products/brake_pad/carlist/honda/HONDA_Accord.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

fields = ['Parttype (category)', 'Parttype url (category)', 'Make', 'Make URL', 'Model', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'contoh.csv'

data = []

iframes = soup.find_all('iframe')
for iframe in iframes:
    src = iframe['src']
    iframe_content = requests.get(src).content
    iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
    tables = iframe_soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')[5:]
        for row in rows:
            # Menghapus kolom yang berisi teks "年式"
            row.find('td', text="年式").extract()
            
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
                    'Parttype (category)': '',
                    'Parttype url (category)': '',
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
