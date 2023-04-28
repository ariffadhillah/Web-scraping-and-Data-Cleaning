# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/autoss-csk-auda1-433303k'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others']
# filename = 'test.csv'


# part_number_element = soup.find('div', class_='product attribute partnumber')
# if part_number_element:
#     try:
#         PartNumber = part_number_element.text.replace('Part No.', '').strip()    
#     except:
#         PartNumber = ''
# else:
#     print(' ')

# try:
#     productTitle = soup.find('h1', class_='page-title').text.strip()    
# except:
#     productTitle = ''

# try:
#     productDescription = soup.find('div', class_='product attribute description').text.strip()    
# except:
#     productDescription = ''

# # gallery-placeholder

# try:
#     imgproductmedia = soup.find('div', {'class': 'product media'})
#     image = imgproductmedia.find('img', {'class': 'gallery-placeholder__image'})
#     image_url = image['src']
# except:
#     image_url = ''
# # try:
# #     price_wrapper = soup.find('span', {'class': 'special-price'})
# #     price = price_wrapper.find('span', {'class': 'price'}).text
# # except:
# #     price = ''

# try:
#     price_wrapper = soup.find('span', {'data-price-type': 'finalPrice'})
#     price = price_wrapper.find('span', {'class': 'price'}).text
# except:
#     price = ''


# # tabel Compatibility 
# try:
#     am_comp = soup.find('div', {'class': 'compatibility-container'})
#     tables = am_comp.find_all('table', class_='ausct')
#     result = {}
#     # list_of_vehicle_compatibility = []
#     for table in tables:
#         brand = ''
#         model = ''
#         modelYears = ''
#         spec_name = ''
#         spec_value = ''
#         rows = table.find_all('tr')
#         for row in rows:
#             if 'class' in row.attrs and 'ausctmh' in row['class']:
#                 brand = row.find('td', {'class': 'acc-head'}).text.strip()
#             elif 'class' in row.attrs and 'ausctmh-container' in row['class']:
#                 model = row.find('td', {'class': 'acc-head'}).text.strip()
#                 if brand not in result:
#                     result[brand] = {}
#                 if model not in result[brand]:
#                     result[brand][model] = {}
#             elif 'class' in row.attrs and 'ausctlh' in row['class']:
#                 modelYears = row.find('td', {'class': 'acc-head'}).text.strip()
#                 if spec_name not in result[brand][model]:
#                     result[brand][model][modelYears] = {}
#             elif 'class' in row.attrs and 'ausctlh' in row['class']:
#                 spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
#                 spec_value = ''
#             elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
#                 spec_container = row.find('td')
#                 spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
#                 spec_value = ','.join(spec_value_parts)
#                 result[brand][model][modelYears][spec_name] = spec_value
#     list_of_vehicle_compatibility = json.dumps(result)
# except:
#     am_comp =''
#     list_of_vehicle_compatibility = ''

# # Specifications / Others
# try:
#     spec_group = soup.find('div', {'class': 'spec-group'})
#     rows = spec_group.find_all('tr')
#     specs = {}
#     for row in rows:
#         key = row.find('th').text.strip().replace(':', '')
#         value = row.find('td').text.strip()
#         specs[key] = value
#     others = json.dumps(specs)
# except:
#     others = ''

# Automotivesuperstore = {
#     'Category (Parent)': '',
#     'Category URL (Parent)': '',
#     'Category - Leaf (Child 1)': '',
#     'Category URL - Leaf (Child 1)': '',
#     'Product URL': '',
#     'PartNumber': PartNumber,
#     'Product Title': productTitle, 
#     'Product Subtitle': '',
#     'Product Description': productDescription,
#     'Image URLs': image_url,
#     'Price': price,
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility.replace('Positions:,', 'Positions":"').replace('"": ', '').replace('Bay,Quantity', 'Bay","Quantity').replace('Quantity Per Vehicle:,', 'Quantity Per Vehicle":"'),
#     'Brand': 'Automotivesuperstore',
#     'OE number / cross-reference': '',
#     'Others': others,
# }

# data.append(Automotivesuperstore)
# print('Saving', Automotivesuperstore['PartNumber'],Automotivesuperstore['Product Title'], Automotivesuperstore['Price'], Automotivesuperstore['List of Vehicle Compatibility'], Automotivesuperstore['Image URLs'], Automotivesuperstore['Product Description'], Automotivesuperstore['Others'])
# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# print('Data is successfully saved in the file', filename)




# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# try:
#     am_comp = soup.find('div', {'class': 'compatibility-container'})
#     print(am_comp)
#     tables = am_comp.find_all('table', class_='ausct')
#     dataresult = []
#     for table in tables:
#         brandresult = ''
#         model = ''
#         others = ''
#         spec_name = ''
#         spec_value = ''

# except:
#     print('Error')


# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# try:
#     am_comp = soup.find('div', {'class': 'compatibility-container'})

#     tables = am_comp.find_all('table', class_='ausct')    
   
#     dataresult = []
#     for table in tables:
#         title = ''
#         brandresult = ''
#         model = ''
#         others = ''
#         spec_name = ''
#         spec_value = ''
        
#         titlebrand = soup.find('tr', class_='ausctmh')
#         make = titlebrand.text.strip()

#         listbrand = soup.find_all('tr', class_='ausctsh')
#         for tr in listbrand:
#             model_list = tr.find_all('td', class_='acc-head')
#             for model in model_list:
#                 model

#             listothers = soup.find_all('tr', class_='ausctlh')
#             for tr in listothers:
#                 others_list = tr.find_all('td', class_='acc-head')
#                 for others in others_list:
#                     others

#                 dataresult.append({
#                     'make': titlebrand.text.strip(),
#                     'model': model.text,
#                     'Others': others.text,
#                 })
#                 print(dataresult)
        
# except:
#     print('Error')



# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# try:
#     am_comp = soup.find('div', {'class': 'compatibility-container'})

#     tables = am_comp.find_all('table', class_='ausct')    
   
#     for table in tables:
#         titlebrand = table.find('tr', class_='ausctmh')
#         make = titlebrand.text.strip()

#         listbrand = table.find_all('tr', class_='ausctsh')
#         for tr in listbrand:
#             model_list = tr.find_all('td', class_='acc-head')
#             for model in model_list:
#                 model_text = model.text


#         listothers = table.find_all('tr', class_='ausctlh')
#         for tr in listothers:
#             others_list = tr.find_all('td', class_='acc-head')
#             for others in others_list:
#                 others_text = others.text
#                 print(others_text)

#             dataresult.append({
#                 'make': make,
#                 'model': model_text,
#                 'Others': others_text,
#             })
        
# except:
#     print('Error')

# print(dataresult)



# import requests
# from bs4 import BeautifulSoup
# import json

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# try:
#     am_comp = soup.find('div', {'class': 'compatibility-container'})

#     tables = am_comp.find_all('table', class_='ausct')    
   
#     for table in tables:
#         titlebrand = table.find('tr', class_='ausctmh')
#         make = titlebrand.text.strip()

#         listbrand = table.find_all('tr', class_='ausctsh')
#         for tr in listbrand:
#             model_list = tr.find_all('td', class_='acc-head')
#             for model in model_list:
#                 model_text = model.text


#         listothers = table.find_all('tr', class_='ausctlh')
#         for tr in listothers:
#             others_list = tr.find_all('td', class_='acc-head')
#             for others in others_list:
#                 others_text = others.text
#                 dataresult.append({
#                     'make': make,
#                     'model': model_text,
#                     'others': others_text,
#                 })
        
# except:
#     print('Error')

# print(json.dumps(dataresult, indent=2))



import requests
from bs4 import BeautifulSoup
import json
import csv

dataresult = []

# membuat permintaan ke URL
url = 'https://automotivesuperstore.com.au/afi-dra1001'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

try:
    am_comp = soup.find('div', {'class': 'compatibility-container'})

    tables = am_comp.find_all('table', class_='ausct')
   
    for table in tables:
        titlebrand = table.find('tr', class_='ausctmh')
        make = titlebrand.text.strip()

        listbrand = table.find_all('tr', class_='ausctsh')
        for tr in listbrand:
            model_list = tr.find_all('td', class_='acc-head')
            for model in model_list:
                model_text = model.text
                listothers = tr.find_next_sibling('tr')
                others_list = listothers.find_all('td', class_='acc-head')
                for others in others_list:
                    others_text = others.text.strip()
                    dataresult.append({"make": make, "model": model_text, "others": others_text})
except:
    print('Error')

print(json.dumps(dataresult, indent=2))
