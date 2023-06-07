# https://webshop.nrf.eu/catalog/category/view/s/automotive/id/41/?v_brand=5087&v_range=124&v_generatie=2016&v_fuel=B&v_size=1.4+%7C+125+KW+%7C+170+HP

# https://webshop.nrf.eu/catalog/category/view/s/automotive/id/41/?v_brand=5087&v_range=500&v_generatie=2008&v_fuel=B&v_size=1.4+%7C+103+KW+%7C+140+HP

# import requests
# from bs4 import BeautifulSoup
import csv
# import json
# import time


# baseurl = 'https://webshop.nrf.eu/catalog/category/view/s/automotive/id/41/?v_brand=5087&v_fuel=B&v_generatie=2008&v_range=500&v_size=1.4+%7C+107+KW+%7C+145+HP'


from bs4 import BeautifulSoup
import requests
import json

baseurl = 'https://webshop.nrf.eu/catalog/category/view/s/sensors-coolant-temperature/id/112/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE part number', 'EAN','DimensionsHeightMM', 'Others']
filename = 'NRF-Example.csv'

data = []
processed_urls = set()

itemlistofVehicleCompatibility = {}

page = 1
while True:
    produclinks = []
    url = f"{baseurl}?p={page}"
    print(url)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productslist = soup.find_all('div', class_='product-wrapper')

    if len(productslist) == 0:
        break

    for item in productslist:
        for link in item.find_all('a', class_='product-url-wrapper', href=True):
            url = link['href']
            if url not in processed_urls:
                produclinks.append(url)
                processed_urls.add(url)

    for product_wrapper in produclinks:
        r = requests.get(product_wrapper, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')


        try:
            productinfomain = soup.find('div', class_='product-info-main')
            categoryParent = productinfomain.find('div', {'class': 'product-type-label'}).contents[0].text.strip()  
            print(categoryParent)  
        except:
            categoryParent = '' 
            
        try:
            productTitle = soup.find('h1', class_='page-title').text.strip()
        except:
            productTitle = '' 
            
        try:
            partNumberdiv = soup.find('div', class_='product attribute sku')
            partNumber = partNumberdiv.find('div',  class_='value' ).text.strip()
        except:
            partNumber = '' 

        try:
            imgproductmedia = soup.find('div', {'class': 'gallery-placeholder'})
            image = imgproductmedia.find('img', {'class': 'gallery-placeholder__image'})
            image_url = image['src']
        except:
            imgproductmedia = ''
            image_url = ''
            
        try:
            infoEANCode = soup.find('div', class_='product-info-label', string='EAN Code')
            eANCode = infoEANCode.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
        except:
            infoEANCode = ''
            eANCode = ''

        try:
            infoDimensionsHeightMM = soup.find('div', class_='product-info-label', string='Height [mm]')
            dimensionsHeightMM = infoDimensionsHeightMM.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
        except:
            infoDimensionsHeightMM = ''
            dimensionsHeightMM = ''

        try:
            infoOE_numbers = soup.find('div', class_='product-info-label', string='OE numbers')
            oEnumbers = infoOE_numbers.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
            oE_numbers = json.dumps([oEnumbers])
        except:
            infoOE_numbers = ''
            oE_numbers = ''

        try:
            infoCross_Number = soup.find('div', class_='product-info-label', string='Cross Number')
            crossNumber = infoCross_Number.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
            cross_Number = json.dumps([crossNumber])
        except:
            infoCross_Number = ''
            cross_Number = ''



        # orther JASON product Info

        product_info = soup.find('div', {'class': 'product-info'})

        data_product_info = {}

        product_labels = product_info.find_all('div', {'class': 'product-info-label'})
        for label in product_labels:
            prop = label.text.strip()
            value = label.find_next_sibling('div', {'class': 'product-info-value'}).text.strip()
            data_product_info[prop] = value

        other_data_product_info = json.dumps(data_product_info)


        webshop = {
            'Category (Parent)': categoryParent,
            'Category URL (Parent)': '',
            'Category - Leaf (Child 1)':'',
            'Category URL - Leaf (Child 1)': '',
            'Product URL': '',
            'PartNumber': partNumber,
            'Product Title': productTitle,
            'Product Subtitle': '',
            'Product Description': '',
            'Image URLs': image_url,
            'Price': '',
            'List of Vehicle Compatibility': '',
            'Brand': 'NRF',
            'OE part number': oE_numbers.replace(' ',', ' ).replace('"','' ),
            'EAN': f"'{eANCode}",
            'DimensionsHeightMM': dimensionsHeightMM,
            'Others':other_data_product_info

        }
        data.append(webshop)
        print('Saving',webshop['Category (Parent)'], webshop['PartNumber'], webshop['Product Title'],webshop['EAN'], )
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item)            
        
    page += 1

# print(len(produclinks))



# list_of_Vehicle_Compatibility = json.dumps(itemlistofVehicleCompatibility)


# print(produclinks)

# testlink = 'https://webshop.nrf.eu/automotive/fiat-10-59.html'

# r = requests.get(testlink, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     productinfomain = soup.find('div', class_='product-info-main')
#     categoryParent = productinfomain.find('div', {'class': 'product-type-label'}).contents[0].text.strip()  
#     print(categoryParent)  
# except:
#     categoryParent = '' 
     
# try:
#     productTitle = soup.find('h1', class_='page-title').text.strip()
# except:
#     productTitle = '' 
     
# try:
#     partNumberdiv = soup.find('div', class_='product attribute sku')
#     partNumber = partNumberdiv.find('div',  class_='value' ).text.strip()
# except:
#     partNumber = '' 

# try:
#     imgproductmedia = soup.find('div', {'class': 'gallery-placeholder'})
#     image = imgproductmedia.find('img', {'class': 'gallery-placeholder__image'})
#     image_url = image['src']
# except:
#     imgproductmedia = ''
#     image_url = ''
     
# try:
#     infoEANCode = soup.find('div', class_='product-info-label', string='EAN Code')
#     eANCode = infoEANCode.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
# except:
#     infoEANCode = ''
#     eANCode = ''

# try:
#     infoDimensionsHeightMM = soup.find('div', class_='product-info-label', string='Height [mm]')
#     dimensionsHeightMM = infoDimensionsHeightMM.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
# except:
#     infoDimensionsHeightMM = ''
#     dimensionsHeightMM = ''

# try:
#     infoOE_numbers = soup.find('div', class_='product-info-label', string='OE numbers')
#     oEnumbers = infoOE_numbers.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
#     oE_numbers = json.dumps([oEnumbers])
# except:
#     infoOE_numbers = ''
#     oE_numbers = ''

# try:
#     infoCross_Number = soup.find('div', class_='product-info-label', string='Cross Number')
#     crossNumber = infoCross_Number.find_next_sibling('div', class_='product-info-value').get_text(strip=True)
#     cross_Number = json.dumps([crossNumber])
# except:
#     infoCross_Number = ''
#     cross_Number = ''



# # orther JASON product Info

# product_info = soup.find('div', {'class': 'product-info'})

# data_product_info = {}

# product_labels = product_info.find_all('div', {'class': 'product-info-label'})
# for label in product_labels:
#     prop = label.text.strip()
#     value = label.find_next_sibling('div', {'class': 'product-info-value'}).text.strip()
#     data_product_info[prop] = value

# other_data_product_info = json.dumps(data_product_info)


# webshop = {
#     'Category (Parent)': categoryParent,
#     'Category URL (Parent)': '',
#     'Category - Leaf (Child 1)':'',
#     'Category URL - Leaf (Child 1)': '',
#     'Product URL': '',
#     'PartNumber': partNumber,
#     'Product Title': productTitle,
#     'Product Subtitle': '',
#     'Product Description': '',
#     'Image URLs': image_url,
#     'Price': '',
#     'List of Vehicle Compatibility': '',
#     'Brand': 'NRF',
#     'OE part number': oE_numbers.replace(' ',', ' ).replace('"','' ),
#     'EAN': f"'{eANCode}",
#     'DimensionsHeightMM': dimensionsHeightMM,
#     'Others':other_data_product_info

# }
# data.append(webshop)
# print('Saving',webshop['Category (Parent)'], webshop['PartNumber'], webshop['Product Title'],webshop['EAN'], )
# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)