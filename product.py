import requests
from bs4 import BeautifulSoup
import csv
import json

baseurl = 'https://www.stanceplus.com'

productURLList = []
data = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

link = 'https://www.stanceplus.com/lowering-springs/SPLS05013A/55421/'
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# try:
#     table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#     car_make = table_list_of_vehicle_compatibility.select_one("td strong").text.strip()
#     car_info = table_list_of_vehicle_compatibility.select_one("tr.bg-white").get_text(separator=", ").strip()
#     car_info = car_info.replace(", ", "", 1)
#     result = {car_make: car_info.rstrip(',')}
#     list_of_vehicle_compatibility = json.dumps(result)
# except:
#     ''

# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = {}

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification[cols[0]] = cols[1]

#     others_specification = json.dumps(dataothers_specification)
# except:
#     others_specification = ''

try:
    price = soup.find('div', class_='item-price').text.strip()
except:
    price = ''

StancedUk = {
    'price': price.replace('A', '') 
    # list_of_vehicle_compatibility.replace(': ', ':').replace(', ', ','),
    # 'Others': others_specification.replace(': ', ':').replace(', ', ',')
}

data.append(StancedUk)

print(data)
fields = ['price']

filename = 'price.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print('data is successfully saved in the file CSV', filename)


# import requests
# from bs4 import BeautifulSoup
# import json

# # Buat request ke website
# url = 'https://www.stanceplus.com/proline-coilovers/SPPCF01093B/55510/'
# r = requests.get(url)

# # Parsing HTML menggunakan BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# # Ambil tabel yang memiliki class 'table table-striped table-bordered'
# table = soup.find('table', {'class': 'table table-striped table-bordered'})

# # Ambil data di dalam setiap baris dan simpan ke dalam dictionary
# data = {}
# rows = table.find_all('tr')
# for row in rows:
#     cols = row.find_all('td')
#     if cols:
#         cols = [col.text.strip().replace('\n', ',') for col in cols]
#         key = cols[0]
#         value = cols[1:]
#         data[key] = value

# # Ubah dictionary menjadi format JSON
# json_data = json.dumps(data)

# # Print hasil
# print(json_data)


# import requests
# from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup as bs
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# productURLList = []
# data = []

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# link = 'https://www.stanceplus.com/proline-coilovers/SPPCF01093B/55510/'
# r = requests.get(link, headers=headers)
# soup = bs(r.content, 'lxml')

# # table = soup.find('table', {'class': 'table table-striped table-bordered'})
# # rows = table.find_all('tr')
# # datarow = json.dumps(rows)
# # print(datarow)

# table = soup.find('table', {'class': 'table table-striped table-bordered'})
# rows = table.find_all('tr')

# # Ambil data di dalam setiap baris dan simpan ke dalam dictionary
# data = {}
# for row in rows:
#     cols = row.find_all('td')
#     if len(cols) >= 2:
#         key = cols[0].text.strip()
#         value = cols[1].text.strip().replace('\n', ', ')
#         data[key] = value

# # Ubah dictionary menjadi format JSON
# json_data = json.dumps(data)

# # Print hasil
# print(json_data)
# data = {}
# for row in rows:
#     cells = row.find_all('td').text
#     print(cells)
    # key = cells[0].find('strong').text
    # value = cells[1].text.replace('\n', '').replace('', ', ').strip()
    # data[key] = value

# json_data = json.dumps(data)
# print(json_data)

# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = {}

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification[cols[0]] = cols[1]

#     others_specification = json.dumps(dataothers_specification)
# except:
#     others_specification = ''
# StancedUk = {
#     # 'List of Vehicle Compatibility': json_data,
#     'Others': others_specification.replace(': ', ':').replace(', ', ',')
# }

# data.append(StancedUk)

# print(data)
# fields = ['List of Vehicle Compatibility', 'Others']

# filename = 'product-Stanced-Uk.csv'

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# print('data is successfully saved in the file CSV', filename)



# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# productURLList = []
# data = []

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# link = 'https://www.stanceplus.com/proline-coilovers/SPPCF01093B/55510/'
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#     table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#     datalist_of_vehicle_compatibility = {}

#     for row in table_rows_list_of_vehicle_compatibility:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         datalist_of_vehicle_compatibility[cols[0]] = cols[1:]
#     list_of_vehicle_compatibility = json.dumps(datalist_of_vehicle_compatibility)

# except:
#     list_of_vehicle_compatibility = ''


# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = {}

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification[cols[0]] = cols[1]

#     others_specification = json.dumps(dataothers_specification)
# except:
#     others_specification = ''


# StancedUk = {
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility,
#     'Others': others_specification,
# }

# data.append(StancedUk)

# print(data)
# fields = ['List of Vehicle Compatibility', 'Others']

# filename = 'product-Stanced-Uk.csv'

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# print('data is successfully saved in the file CSV', filename)



# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# productURLList = []
# data = []

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# link = 'https://www.stanceplus.com/proline-coilovers/SPPCF01093B/55510/'
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#     table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#     datalist_of_vehicle_compatibility = []

#     for row in table_rows_list_of_vehicle_compatibility:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         datalist_of_vehicle_compatibility.append(cols)
#     list_of_vehicle_compatibility = json.dumps(datalist_of_vehicle_compatibility)

# except:
#     list_of_vehicle_compatibility = ''


# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = {}

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification[cols[0]] = cols[1]

#     others_specification = json.dumps(dataothers_specification)
# except:
#     others_specification = ''

# StancedUk = {
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility,
#     'Others': others_specification,
# }

# data.append(StancedUk)

# print(data)
# fields = ['List of Vehicle Compatibility', 'Others']

# filename = 'product-Stanced-Uk.csv'

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# print('data is successfully saved in the file CSV', filename)



# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# productURLList = []
# data = []

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# link = 'https://www.stanceplus.com/proline-coilovers/SPPCF01093B/55510/'
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#     table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#     datalist_of_vehicle_compatibility = {}

#     for row in table_rows_list_of_vehicle_compatibility:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         datalist_of_vehicle_compatibility[cols] = cols
#     list_of_vehicle_compatibility = json.dumps(datalist_of_vehicle_compatibility)

# except:
#     list_of_vehicle_compatibility = ''


# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = {}

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification[cols[0]] = cols[1]

#     others_specification = json.dumps(dataothers_specification)
# except:
#     others_specification = ''


# StancedUk = {
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility,
#     'Others': others_specification,
# }

# data.append(StancedUk)

# print(data)
# fields = ['List of Vehicle Compatibility', 'Others']

# filename = 'product-Stanced-Uk.csv'

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# print('data is successfully saved in the file CSV', filename)




# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# productURLList = []
# data = []

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# link = 'https://www.stanceplus.com/proline-coilovers/SPPCF01093B/55510/'
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# others_specification = None
# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = []

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification.append(cols)

#     json_data = json.dumps(dataothers_specification)

#     others_specification = str(dataothers_specification).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")
# except:
#     pass

# list_of_vehicle_compatibility = None
# try:
#     table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#     table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#     datalist_of_vehicle_compatibility = []

#     for row in table_rows_list_of_vehicle_compatibility:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         datalist_of_vehicle_compatibility.append(cols)

#     list_of_vehicle_compatibility = str(datalist_of_vehicle_compatibility).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")

# except:
#     pass

# StancedUk = {
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility ,
#     'Others': others_specification,
# }

# data.append(StancedUk)

# print(data)
# fields = ['List of Vehicle Compatibility', 'Others']

# filename = 'product-Stanced-Uk.csv'

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow({field: item[field] for field in fields})

# print('data is successfully saved in the file CSV', filename)




# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# productURLList = []
# data = []

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# link = 'https://www.stanceplus.com/proline-coilovers/SPPCF01027B/55523/'
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#     table_rows_Specification = table_Specification.find_all('tr')
#     dataothers_specification = []

#     for row in table_rows_Specification:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification.append(cols)

#         json_data = json.dumps(dataothers_specification)

#         others_specification = str(dataothers_specification).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")
# except:
#     ' '

# try:
#     table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#     table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#     datalist_of_vehicle_compatibility = []

#     for row in table_rows_list_of_vehicle_compatibility:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         datalist_of_vehicle_compatibility.append(cols)

#         list_of_vehicle_compatibility  = str(datalist_of_vehicle_compatibility).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")

#         json_data = json.dumps(list_of_vehicle_compatibility )
# except:
#     ' '

# StancedUk = {
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility ,
#     'Others': others_specification,
# }

# data.append(StancedUk)

# print(data)
# fields = ['List of Vehicle Compatibility', 'Others']

# filename = 'product-Stanced-Uk.csv'

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# print('data is successfully saved in the file CSV', filename)




# import requests
# from bs4 import BeautifulSoup
# import csv
# import json


# baseurl = 'https://www.stanceplus.com'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# r = requests.get('https://www.stanceplus.com')
# soup = BeautifulSoup(r.content, 'lxml')

# categorylinks  = []
# categorylist = soup.find_all('ul', class_='col-6 col-md-3 col-lg-2')

# for itemcategorylist in categorylist:
#     for linkcategory in itemcategorylist.find_all('a', href=True):
#         categorylinks.append(baseurl + linkcategory['href'])

# productList = []
# data = []
# for linkcategory in categorylinks:
#     r = requests.get(linkcategory, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     productItem = soup.find_all('div', class_='panel-collapse collapse')
#     for item in productItem:
#         for href in item.find_all('a', class_='', href=True ):
#             url = baseurl + href['href']
#             if url not in productList:  # check for duplicates
#                 productList.append(url)


#     for productURL in productList:
#             r = requests.get(productURL, headers=headers)
#             soup = BeautifulSoup(r.content, 'lxml')

#             productTitle = soup.find('h1', class_='item-title').text.strip()

#             try:
#                 productSubtitle = soup.find('h2', class_='item-title').text.strip()
#             except:
#                 productSubtitle = ''
#             try:
#                 price = soup.find('div', class_='item-price').text.strip()
#             except:
#                 price = ''
            
#             sectionimage_url = soup.find('section', {'class': 'hero'})        
#             try:
#                 image_url = baseurl + sectionimage_url.find('a', {'class': 'image'}).get('href')
#             except:
#                 image_url = ' '    

#             try:
#                 table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#                 table_rows_Specification = table_Specification.find_all('tr')
#                 dataothers_specification = []

#                 for row in table_rows_Specification:
#                     cols = row.find_all('td')
#                     cols = [col.text.strip() for col in cols]
#                     dataothers_specification.append(cols)
#                     json_data = json.dumps(dataothers_specification)

#                     others_specification = str(dataothers_specification).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")
#             except:
#                 ' '

#             try:
#                 table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#                 table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#                 datalist_of_vehicle_compatibility = []

#                 for row in table_rows_list_of_vehicle_compatibility:
#                     cols = row.find_all('td')
#                     cols = [col.text.strip() for col in cols]
#                     datalist_of_vehicle_compatibility.append(cols)

#                 list_of_vehicle_compatibility  = str(datalist_of_vehicle_compatibility).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")

#                 json_data = json.dumps(list_of_vehicle_compatibility )
#             except:
#                 ' '

#             StancedUk = {
#                 'Category (Parent)': linkcategory.split('/')[-1].replace('-', ' ').title(),
#                 'Category URL (Parent)': linkcategory,
#                 'Category - Leaf (Child 1)': '',
#                 'Category URL - Leaf (Child 1)': '',
#                 'Product URL': productURL,
#                 'PartNumber': productURL.split("/")[-2],
#                 'Product Title': productTitle, 
#                 'Product Subtitle': productSubtitle,
#                 'Product Description': '',
#                 'Image URLs': image_url,
#                 'Price': price,
#                 'List of Vehicle Compatibility': list_of_vehicle_compatibility,
#                 'Brand': 'STANCED UK',
#                 'OE number / cross-reference': '',
#                 'Others': others_specification
#             }

#             data.append(StancedUk)
#             print('Saving: ', StancedUk['Product Title'], StancedUk['Product URL'], StancedUk['PartNumber'])

#             fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others']

#             filename = 'test-Stanced-Uk-product.csv'

#             with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#                 writer = csv.DictWriter(csvfile, fieldnames=fields)
#                 writer.writeheader()
#                 for item in data:
#                     writer.writerow(item)

# print('data is successfully saved in the file CSV', filename)




# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://www.stanceplus.com'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }

# r = requests.get('https://www.stanceplus.com')
# soup = BeautifulSoup(r.content, 'lxml')

# categorylinks  = []
# categorylist = soup.find_all('ul', class_='col-6 col-md-3 col-lg-2')

# for itemcategorylist in categorylist:
#     for linkcategory in itemcategorylist.find_all('a', href=True):
#         categorylinks.append(baseurl + linkcategory['href'])

# data = []
# for linkcategory in categorylinks:
#     productList = []  # reset the product list for each category
#     r = requests.get(linkcategory, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     productItem = soup.find_all('div', class_='panel-collapse collapse')
#     for item in productItem:
#         for href in item.find_all('a', class_='', href=True ):
#             url = baseurl + href['href']
#             if url not in productList:  # check for duplicates within the category
#                 productList.append(url)

#     for productURL in productList:
#         r = requests.get(productURL, headers=headers)
#         soup = BeautifulSoup(r.content, 'lxml')
        
#         try:
#             productTitle = soup.find('h1', class_='item-title').text.strip()
#         except:
#             productTitle = ''
        
#         try:
#             productSubtitle = soup.find('h2', class_='item-title').text.strip()
#         except:
#             productSubtitle = ''
        
#         try:
#             ProductDescription = soup.find('div', class_='tab-pane fade font-14 bullets').text.strip()
#         except:
#             ProductDescription = ''

#         sectionimage_url = soup.find('section', {'class': 'hero'})
#         try:
#             image_url = baseurl + sectionimage_url.find('a', {'class': 'image'}).get('href')
#         except:
#             image_url = ' '

#         try:
#             price = soup.find('div', class_='item-price').text.strip()
#         except:
#             price = ''

#         try:
#             table_Specification = soup.find('table', {'class': 'table table-striped table-bordered font-14'})
#             table_rows_Specification = table_Specification.find_all('tr')
#             dataothers_specification = []

#             for row in table_rows_Specification:
#                 cols = row.find_all('td')
#                 cols = [col.text.strip() for col in cols]
#                 dataothers_specification.append(cols)

#             json_data = json.dumps(dataothers_specification)

#             others_specification = str(dataothers_specification).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")
#         except:
#             ' '

#         try:
#             table_list_of_vehicle_compatibility = soup.find('table', {'class': 'table table-striped table-bordered'})
#             table_rows_list_of_vehicle_compatibility = table_list_of_vehicle_compatibility.find_all('tr')
#             datalist_of_vehicle_compatibility = []

#             for row in table_rows_list_of_vehicle_compatibility:
#                 cols = row.find_all('td')
#                 cols = [col.text.strip() for col in cols]
#                 datalist_of_vehicle_compatibility.append(cols)

#             list_of_vehicle_compatibility  = str(datalist_of_vehicle_compatibility).replace("[[", "{").replace("]]", "}").replace("[", "").replace("]", "").replace("'", "")

#             json_data = json.dumps(list_of_vehicle_compatibility )
#         except:
#             ' '


#         StancedUk = {
#             'Category (Parent)': linkcategory.split('/')[-1].replace('-', ' ').title(),
#             'Category URL (Parent)': linkcategory,
#             'Category - Leaf (Child 1)': '',
#             'Category URL - Leaf (Child 1)': '',
#             'Product URL': productURL,
#             'PartNumber': productURL.split("/")[-2],
#             'Product Title': productTitle, 
#             'Product Subtitle': productSubtitle,
#             'Product Description': ProductDescription,
#             'Image URLs': image_url,
#             'Price': price,
#             'List of Vehicle Compatibility': list_of_vehicle_compatibility,
#             'Brand': 'STANCED UK',
#             'OE number / cross-reference': '',
#             'others': others_specification,
#         }

#         data.append(StancedUk)
#         print('Saving: ', StancedUk['Product Title'], StancedUk['Product URL'], StancedUk['PartNumber'])

# fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'others']

# filename = 'Stanced-Uk-succes.csv'

