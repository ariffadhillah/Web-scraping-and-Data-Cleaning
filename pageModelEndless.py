import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}


# fields = ['Parttype (category)', 'Parttype URL (category)', 'Make', 'Make URL', 'Model', 'Model URL', 'Series', 'Year', 'Engine cc', 'Type', 'PartNumber']
# filename = 'endlessmodel.csv'

data = []


processed_urls = set()


categoryProduct = []






urllistimport1 = ['https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_BMW.html']

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

        # model = ''  # Inisialisasi variabel model di sini
        for table in tablesimport:
            rows = table.find_all('tr')[6:]
            for row in rows:
                removetext = ['フロント']
                if any(text in td.text.strip() for td in row for text in removetext):
                    continue
                if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                    continue


                try:
                    td_elementmodel = row.find_all('td')
                    if len(td_elementmodel) == 21:
                        model = td_elementmodel[1].text.strip()
                    elif len(td_elementmodel) == 21:
                        model = td_elementmodel[1].text.strip()
                    else:
                        model = ''
                except:
                    model = ''

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

                if make:
                    endless = {
                        'Parttype (category)': 'ブレーキパッド',
                        'Parttype URL (category)': 'https://www.endless-sport.co.jp/products/brake_pad/index.html',
                        'Make': 'Make ' + make,
                        'Make URL': 'urlimportlist',
                        'Model': 'Model ' + model,
                        'Model URL': 'urlimportlist',
                        "Series": "Series  " + modelSeries,
                        'Year': 'Year  ' + years,
                        'Engine cc': '',
                        'Type': '',
                        'PartNumber': 'PartNumber ' + partNumber.replace(' ', '\n'),
                    }
                    # if modelSeries and years:
                    data.append(endless)
                    print('Saving', endless['Parttype (category)'], endless['Make URL'], endless['Make'], endless['Model'], endless['Type'], endless['Year'], endless['Series'], endless['PartNumber'])


