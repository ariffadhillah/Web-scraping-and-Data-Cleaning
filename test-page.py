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

pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

r = requests.get(pageBrakepads, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


listCarsName = []
brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
carList = brakepad_search_whole.find('div', id='right_menu_box')
for linkcars in carList.find_all('a', href=True):
    listCarsName.append(linkcars['href'])

fields = ['Parttype (category)', 'Parttype url (category)', 'Make', 'Make URL', 'Model', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'endless.csv'

productList = []
for carName in listCarsName:
    urlcar = requests.get(carName, headers=headers)
    soup = BeautifulSoup(urlcar.content, 'lxml')
    carNameIcons = soup.find_all('div', id='ewig_pad_whole')
    for itemCarName in carNameIcons:
        for href in itemCarName.find_all('a',  href=True):
            url = href['href']
            if url not in processed_urls:
                productList.append(pageBrakepads.replace('/car_list.html', '/') + url)
                processed_urls.add(url)
            time.sleep(.5)
        for pageCarlist in productList:            
            r = requests.get(pageCarlist, headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')            
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
                        if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                            continue  
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

# page 
importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
listImportedCar = []
for linkcarsimported in importedCar.find_all('a', href=True):
    listImportedCar.append(linkcarsimported['href'])
# print(len(listImportedCar))
print(listImportedCar)

