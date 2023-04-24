import requests
from bs4 import BeautifulSoup
import csv
import json

baseurl = 'https://www.stanceplus.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

r = requests.get('https://www.stanceplus.com')
soup = BeautifulSoup(r.content, 'lxml')

categorylinks  = []
categorylist = soup.find_all('ul', class_='col-6 col-md-3 col-lg-2')

for itemcategorylist in categorylist:
    for linkcategory in itemcategorylist.find_all('a', href=True):
        categorylinks.append(baseurl + linkcategory['href'])

data = []
for linkcategory in categorylinks:
    r = requests.get(linkcategory, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productItem = soup.find_all('div', class_='panel-collapse collapse')
    for item in productItem:
        productList = []
        for href in item.find_all('a', class_='', href=True):
            url = baseurl + href['href']
            if url not in productList:
                productList.append(url)

        for productURL in productList:
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
                table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
                datalist_of_vehicle_compatibility = []

                for row in table_rows_list_of_vehicle_compatibility:
                    cols = row.find_all('td')
                    cols = [col.text.strip() for col in cols]
                    datalist_of_vehicle_compatibility.append(cols)

                list_of_vehicle_compatibility = str(datalist_of_vehicle_compatibility).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")

                json_data = json.dumps(list_of_vehicle_compatibility)
            except:
                list_of_vehicle_compatibility = ''

            try:
                table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
                table_rows_Specification = table_Specification.find_all('tr')
                others_specification = []

                for row in table_rows_Specification:
                    cols = row.find_all('td')
                    cols = [col.text.strip() for col in cols]
                    others_specification.append(cols)
                json_data = json.dumps(others_specification)
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
                'List of Vehicle Compatibility': list_of_vehicle_compatibility,
                'Brand': 'STANCED UK',
                'OE number / cross-reference': '',
                'Others': others_specification,
            }

            data.append(StancedUk)
            print('Saving: ', StancedUk['Product Title'], StancedUk['Product URL'], StancedUk['PartNumber'])

            fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others']

            filename = 'Stanced-Uk-succes-file.csv'

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for item in data:
                    writer.writerow(item)

print('data is successfully saved in the file CSV', filename)


