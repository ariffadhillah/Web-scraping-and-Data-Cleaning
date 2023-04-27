import requests
from bs4 import BeautifulSoup
import csv
import json

baseurl = 'https://www.stanceplus.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

categorylinks = []
r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
categorylist = soup.find_all('ul', class_='col-6 col-md-3 col-lg-2')
for itemcategorylist in categorylist:
    for linkcategory in itemcategorylist.find_all('a', href=True):
        categorylinks.append(baseurl + linkcategory['href'])

data = []
processed_urls = set()
fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others']
filename = 'Stanced-Uk.csv'

for linkcategory in categorylinks:
    r = requests.get(linkcategory, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    # productItem = soup.find_all('div', class_='panel-collapse collapse')
    productItem = soup.find_all('div', class_='panel panel-default panel-make')
    for item in productItem:
        productList = []
        for href in item.find_all('a', class_='', href=True):
            url = baseurl + href['href']
            if url not in productList:
                productList.append(url)
        for productURL in productList:
            if productURL not in processed_urls:
                r = requests.get(productURL, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')


                try:
                    productTitle = soup.find('h1', class_='item-title').text.strip()
                except:
                    productTitle = ' '

                try:
                    productSubtitle = soup.find('h2', class_='item-title').text.strip()
                except:
                    productSubtitle = ''

                try:
                    price = soup.find('div', class_='item-price').text.strip()
                except:
                    price = ''
                
                try:
                    ProductDescription = soup.find('div', class_='tab-pane fade font-14 bullets').text.strip()
                except:
                    ProductDescription = ''

                sectionimage_url = soup.find('section', {'class': 'hero'})
                try:
                    image_url = baseurl + sectionimage_url.find('a', {'class': 'image'}).get('href')
                except:
                    image_url = ''

                try:
                    table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
                    car_make = table_list_of_vehicle_compatibility.select_one("td strong").text.strip()
                    car_info = table_list_of_vehicle_compatibility.select_one("tr.bg-white").get_text(separator=", ").strip()
                    car_info = car_info.replace(", ", "", 1)
                    result = {car_make: car_info.rstrip(',')}
                    list_of_vehicle_compatibility = json.dumps(result)
                except:
                    ''
                try:
                    table_Specification = soup.find('div', {'class': 'compatibility-container'})
                    table_rows_Specification = table_Specification.find_all('tr')
                    dataothers_specification = {}

                    for row in table_rows_Specification:
                        cols = row.find_all('td')
                        cols = [col.text.strip() for col in cols]
                        dataothers_specification[cols[0]] = cols[1]

                    others_specification = json.dumps(dataothers_specification)
                except:
                    others_specification = ''

                StancedUk = {
                    'Category (Parent)': linkcategory.split('/')[-1].replace('-', ' ').title(),
                    'Category URL (Parent)': linkcategory,
                    'Category - Leaf (Child 1)': '',
                    'Category URL - Leaf (Child 1)': '',
                    'Product URL': productURL,
                    'PartNumber': productURL.split("/")[-2],
                    'Product Title': productTitle, 
                    'Product Subtitle': productSubtitle,
                    'Product Description': ProductDescription,
                    'Image URLs': image_url,
                    'Price': price,
                    'List of Vehicle Compatibility': list_of_vehicle_compatibility.replace(': ', ':').replace(', ', ','),
                    'Brand': 'STANCED UK',
                    'OE number / cross-reference': '',
                    'Others': others_specification.replace(': ', ':').replace(', ', ',')
                }

                data.append(StancedUk)
                print('Saving', StancedUk['Category (Parent)'], StancedUk['Product URL'], StancedUk['PartNumber'])
                processed_urls.add(productURL)

                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)

print('Data is successfully saved in the file', filename)


# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)
# print('Data is successfully saved in the file', filename)
