# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# # Set the base URL and user agent
# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# # Create a set to store processed URLs to avoid duplicates
# processed_urls = set()

# # Create a list to store category product names
# categoryProduct = []

# # Set the URL for brake pads category and get the page content
# pageBrakepads = baseurl + '/products/brake_pad/car_list.html'
# r = requests.get(pageBrakepads, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# # Find all the car names on the brake pads category page
# listCarsName = []
# brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
# carList = brakepad_search_whole.find('div', id='right_menu_box')
# for linkcars in carList.find_all('a', href=True):
#     listCarsName.append(linkcars['href'])

# # Set the field names for the CSV file
# fields = ['Year', 'Engine cc', 'Type']
# filename = 'contoh.csv'

# # Create a list to store all product URLs for all car models
# productList = []

# # Loop through all car models and get their product URLs
# for carName in listCarsName:
#     urlcar = requests.get(carName, headers=headers)
#     soup = BeautifulSoup(urlcar.content, 'lxml')
#     carNameIcons = soup.find_all('div', id='ewig_pad_whole')
#     for itemCarName in carNameIcons:
#         for href in itemCarName.find_all('a',  href=True):
#             # Append product URL to the list only if it hasn't been processed before
#             url = href['href']
#             if url not in processed_urls:
#                 productList.append(baseurl + url)
#                 processed_urls.add(url)
#             time.sleep(.5)
            
# # Loop through all product URLs and save the product data to CSV file
# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for pageCarlist in productList:
#         r = requests.get(pageCarlist, headers=headers)
#         soup = BeautifulSoup(r.content, 'lxml')
#         time.sleep(.1)
#         data = []
#         iframes = soup.find_all('iframe')
#         for iframe in iframes:
#             src = iframe['src']
#             iframe_content = requests.get(src).content
#             iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#             tables = iframe_soup.find_all('table')
#             for table in tables:
#                 rows = table.find_all('tr')[5:]
#                 for row in rows:
#                     if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#                         continue
#                     year = row.find_all('td')[1].text.strip().replace('～', ' ～ ')
#                     engine = row.find_all('td')[2].text.strip()
#                     type_ = row.find_all('td')[3].text.strip()
#                     endless = {
#                         'Year': year,
#                         'Engine cc': engine,
#                         'Type': type_,
#                     }
#                     data.append(endless)
#                     print('Saving',endless['Make'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])



import requests
from bs4 import BeautifulSoup
import csv

# first URL
url1 = "https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_ALFAROMEO.html"
# second URL
url2 = "https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_LOTUS.html"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

fields = ['Make','Model','Year','PartNumber']
filename = 'Example.csv'
data = []

# function to scrape data from a table and append to the data list
def scrape_data(make, model, rows):
    for row in rows:
        if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
            continue
        year = row.find_all('td')
        PartNumberFront = row.find_all('td')
        PartNumberRear = row.find_all('td')[10:]
        if PartNumberFront and PartNumberRear:
            PartNumber = PartNumberFront[5].text.strip() +' '+ PartNumberRear[0].text.strip()
        else:
            PartNumber = ""            
        if year  and PartNumber:
            endless = {
                'Make': make,
                'Model': model,                  
                'Year': year[3].text.strip().replace('～', ' ～ '),
                'PartNumber': PartNumber.replace(' ', '\n'),
            }
            data.append(endless)
            print('Saving', endless['Make'], endless['Model'], endless['Year'], endless['PartNumber'])                

# scrape data from the first URL
r = requests.get(url1, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
iframesimport = soup.find_all('iframe')
for iframeimport in iframesimport:
    src = iframeimport['src']
    iframeimport_content = requests.get(src).content
    iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
    tablesimport = iframeimport_soup.find_all('table')
    for tableMake in tablesimport:
        rowsMake = tableMake.find_all('tr')[1]
        makeimport =  rowsMake.find_all('td')[1]
    for tablemodelimport in tablesimport:
        rowsmodelimport = tablemodelimport.find_all('tr')[2]
        modelimport =  rowsmodelimport.find_all('td')[1]
    rows = []
    for table in tablesimport:
        rows += table.find_all('tr')[5:]
    scrape_data(makeimport.text.strip(), modelimport.text.strip(), rows)


# scrape data from the second URL
# scrape data from the second URL
hreflink = "https://www.endless-sport.co.jp/products/brake_pad/BrakePad_Carlist/import/BrakePad_LOTUS.html"
r = requests.get(hreflink, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
data2 = []
iframesimport = soup.find_all('iframe')
for iframeimport in iframesimport:
    src = iframeimport['src']
    iframeimport_content = requests.get(src).content
    iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
    tablesimport = iframeimport_soup.find_all('table')
    for tableMake in tablesimport:
        rowsMake = tableMake.find_all('tr')[1]
        makeimport =  rowsMake.find_all('td')[1]
        for tablemodelimport in tablesimport:
            rowsModelimport = tablemodelimport.find_all('tr')
            for rowModelimport in rowsModelimport:
                colsModelimport = rowModelimport.find_all('td')
                colsModelimport = [ele.text.strip() for ele in colsModelimport]
                data2.append([makeimport.text.strip(), colsModelimport[0], colsModelimport[1], colsModelimport[2]])
print(data2)
