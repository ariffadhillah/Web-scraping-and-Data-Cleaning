import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

data = []


processed_urls = set()


categoryProduct = []


# urllistimport1 = [
#     'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_AUDI.html',
#     'https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_MERCEDES.html'
# ]

# data = []

# for urlimportlist in urllistimport1:
#     r = requests.get(urlimportlist, verify=False)
#     soup = BeautifulSoup(r.content, 'lxml')

#     iframesimport = soup.find_all('iframe')
#     for iframeimport in iframesimport:
#         src = iframeimport['src']
#         iframeimport_content = requests.get(src).content
#         iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#         tablesimport = iframeimport_soup.find_all('table')

#         for tablemodelimport in tablesimport:
#             rowsmodelimport = tablemodelimport.find_all('tr')[2]
#             modelimport = rowsmodelimport.find_all('td')[1]

#         for table in tablesimport:
#             rows = table.find_all('tr')[5:]
#             for row in rows:
#                 removetext = [
#                     '※1 EIP132かEIP149のいずれかになります。形状図にてご確認ください。',
#                     '※2 EIP159、EIP162、EIP165、EIP232の価格は他の品番と異なりますのでご注意ください.'
#                 ]
#                 if any(text in td.text.strip() for td in row for text in removetext):
#                     continue
#                 # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
#                 if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#                     continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
#                 try:
#                     td_elementsmodel = row.find_all('td')
#                     if len(td_elementsmodel) == 12:
#                         model = td_elementsmodel[1].text.strip()
#                     else:
#                         model = ''
#                 except:
#                     model = ''
#                 try:
#                     td_elementsseries = row.find_all('td')
#                     if len(td_elementsseries) == 12:
#                         series = td_elementsseries[5].text.strip()
#                     else:
#                         series = ''
#                 except:
#                     series = ''
#                 try:
#                     td_elementsyears = row.find_all('td')
#                     if len(td_elementsyears) == 12:
#                         years = td_elementsyears[4].text.strip()
#                     else:
#                         years = ''
#                 except:
#                     years = ''

#                 partNumberFront = row.find_all('td')
#                 partNumberRear = row.find_all('td')[9:]
#                 if partNumberFront and partNumberRear:
#                     partNumber = partNumberFront[6].text.strip() + ' ' + partNumberRear[0].text.strip()
#                 else:
#                     partNumber = ""

#                 endless = {
#                     'Parttype (category)': 'ブレーキパッド',
#                     'Parttype URL (category)': 'https://www.endless-sport.co.jp/products/brake_pad/index.html',
#                     'Make': modelimport.text.strip(),
#                     'Make URL': urlimportlist,
#                     'Model': model,
#                     'Model URL': '',
#                     "Series": series,
#                     'Year': years,
#                     'Engine cc': '',
#                     'Type': '',
#                     'PartNumber': partNumber.replace(' ', '\n'),
#                 }
#                 if model and partNumber:
#                     data.append(endless)
#                     print('Saving', endless['Make'], endless['Model'], endless['Type'], endless['Year'],
#                           endless['Series'], endless['PartNumber'])


import requests
from bs4 import BeautifulSoup
data = []


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
                print('Saving', endless['Parttype (category)'],  endless['Make'], endless['Model'], endless['Type'], endless['Year'],  endless['Series'],  endless['PartNumber'])
