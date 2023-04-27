# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# # import json

# # baseurl = 'https://automotivesuperstore.com.au'
# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# # }

# # # linkCategoryProduct = 'https://automotivesuperstore.com.au/autoss-csk-auda3-4100043k'
# # linkCategoryProduct = 'https://automotivesuperstore.com.au/dayco-kpt210'
# # r = requests.get(linkCategoryProduct, headers=headers)
# # soup = BeautifulSoup(r.content, 'lxml')


# # part_number_element = soup.find('div', class_='product attribute partnumber')
# # if part_number_element:
# #     try:
# #         PartNumber = part_number_element.text.replace('Part No.', '').strip()    
# #     except:
# #         PartNumber = ''
# # else:
# #     print(' ')

# # try:
# #     productTitle = soup.find('h1', class_='page-title').text.strip()    
# # except:
# #     productTitle = ''

# # try:
# #     productDescription = soup.find('div', class_='product attribute description').text.strip()    
# # except:
# #     productDescription = ''

# # table = soup.find('div', {'class': 'compatibility-container'})

# # # Mencari semua row dalam table
# # rows = table.find_all('tr')

# # # Menginisialisasi dictionary untuk menampung data
# # data = {}

# # # Looping untuk setiap row dalam table
# # for row in rows:
# #     # Mencari kolom-kolom dalam row
# #     cols = row.find_all('td')
    
# #     # Mengekstrak teks dari kolom pertama dan kedua
# #     key = cols[0].get_text().strip()
# #     value = cols[1].get_text().strip()
    
# #     # Menambahkan data ke dalam dictionary
# #     data[key] = value

# # # Mengubah dictionary ke dalam format JSON
# # json_data = json.dumps(data)

# # # Mencetak data JSON
# # print(json_data)


# # print(PartNumber, productTitle, productDescription, json_data)

# import requests
# from bs4 import BeautifulSoup
# import json

# baseurl = 'https://automotivesuperstore.com.au'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# # linkCategoryProduct = 'https://automotivesuperstore.com.au/autoss-csk-auda3-4100043k'
# linkCategoryProduct = 'https://automotivesuperstore.com.au/dayco-kpt210'
# r = requests.get(linkCategoryProduct, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')


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

# table = soup.find('table', {'class': 'ausct'})

# # Mencari semua row dalam table
# rows = table.find_all('tr', class_='ausctsh-container')
# print(rows)

# # Menginisialisasi dictionary untuk menampung data
# data = {}

# # Looping untuk setiap row dalam table
# # for row in rows:
# #     # Mencari kolom-kolom dalam row
# #     cols = row.find_all('td', class_='acc-head')
    
# #     # Mengekstrak teks dari kolom pertama dan kedua
# #     key = cols[0].get_text().strip()
    
# #     # Cek apakah kolom kedua ada atau tidak
# #     if len(cols) > 1:
# #         value = cols[1].get_text().strip()
# #     else:
# #         value = ''
    
# #     # Menambahkan data ke dalam dictionary
# #     data[key] = value

# # # Mengubah dictionary ke dalam format JSON
# # json_data = json.dumps(data)

# # # Mencetak data JSON
# # print(json_data)


# print(PartNumber, productTitle, productDescription)



# import requests
# from bs4 import BeautifulSoup
# import json

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/dayco-kpt210'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# # mencari elemen HTML dengan id="am_comp"
# am_comp = soup.find('div', {'class': 'compatibility-container'})

# # mencari semua elemen tabel di dalam elemen HTML dengan id="am_comp"
# tables = am_comp.find_all('table', class_='ausct')

# # membuat dictionary kosong untuk menyimpan hasil
# result = {}
# dataothers_specification = {}
# # mengambil teks dalam tabel dan menyimpannya dalam dictionary
# for table in tables:
#     # print(table)
#     rows = table.find_all('tr')
#     for row in rows:       
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         dataothers_specification[cols[0]] = cols[1:]

#     others_specification = json.dumps(dataothers_specification)
#     print(others_specification)

# import requests
# from bs4 import BeautifulSoup
# import json

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/dayco-kpt210'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# try:

#     # mencari elemen HTML dengan id="am_comp"
#     am_comp = soup.find('div', {'class': 'compatibility-container'})

#     # mencari semua elemen tabel di dalam elemen HTML dengan id="am_comp"
#     tables = am_comp.find_all('table', class_='ausct')

#     # membuat dictionary kosong untuk menyimpan hasil
#     result = {}

#     # mengambil teks dalam tabel dan menyimpannya dalam dictionary
#     for table in tables:
#         brand = ''
#         model = ''
#         rows = table.find_all('tr')
#         for row in rows:
#             if 'class' in row.attrs and 'ausctmh' in row['class']:
#                 brand = row.find('td', {'class': 'acc-head'}).text.strip()
#                 if brand not in result:
#                     result[brand] = {}
#             elif 'class' in row.attrs and 'ausctsh' in row['class']:
#                 model = row.find('td', {'class': 'acc-head'}).text.strip()
#                 if model not in result[brand]:
#                     result[brand][model] = {}
#             elif 'class' in row.attrs and 'ausctlh' in row['class']:
#                 spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
#                 spec_value = ''
#             elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
#                 spec_value = row.find('td').text.strip()
#                 result[brand][model][spec_name] = spec_value

#     # mengubah hasil menjadi format json dan menampilkan
#     json_result = json.dumps(result, indent=4)
#     print(json_result)
# except:
#     am_comp = ''




# import requests
# from bs4 import BeautifulSoup
# import json

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/dayco-kpt218#compatibility'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')


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

# sectionimage_url = soup.find('div', {'class': 'fotorama__stage__frame fotorama_vertical_ratio fotorama__loaded fotorama__loaded--img fotorama__active'})
# try:
#     image_url = sectionimage_url.find('img', {'class': 'fotorama__img'}).get('href')
# except:
#     image_url = ''
    
# try:
#     # mencari elemen HTML dengan class "compatibility-container"
#     am_comp = soup.find('div', {'class': 'compatibility-container'})

#     # mencari semua elemen tabel di dalam elemen HTML dengan class "ausct"
#     tables = am_comp.find_all('table', class_='ausct')

#     # membuat dictionary kosong untuk menyimpan hasil
#     result = {}

#     # mengambil teks dalam tabel dan menyimpannya dalam dictionary
#     for table in tables:
#         brand = ''
#         model = ''
#         rows = table.find_all('tr')
#         for row in rows:
#             if 'class' in row.attrs and 'ausctmh' in row['class']:
#                 brand = row.find('td', {'class': 'acc-head'}).text.strip()
#                 if brand not in result:
#                     result[brand] = {}
#             elif 'class' in row.attrs and 'ausctsh' in row['class']:
#                 model = row.find('td', {'class': 'acc-head'}).text.strip()
#                 if model not in result[brand]:
#                     result[brand][model] = {}
#             elif 'class' in row.attrs and 'ausctlh' in row['class']:
#                 spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
#                 spec_value = ''
#             elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
#                 spec_container = row.find('td')
#                 spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
#                 spec_value = '"' .join(spec_value_parts)
#                 spec_value = spec_value 
#                 result[brand][model][spec_name] = spec_value.replace(':,',':')

#     # mengubah hasil menjadi format json dan menampilkan
#     list_of_vehicle_compatibility = json.dumps(result, indent=4)

# except:
#     am_comp = ''

# StancedUk = {
#     'PartNumber': PartNumber,
#     'Product Title': productTitle, 
#     'List of Vehicle Compatibility': list_of_vehicle_compatibility.replace('\n', '').replace('\\', '').replace('Quantity Per Vehicle:', ' , "Quantity Per Vehicle: '),
#     'Image url': image_url,
#     'Brand': 'Automotivesuperstore',
#     'OE number / cross-reference': '',
# }

# data.append(StancedUk)

# print(data)



# import requests
# from bs4 import BeautifulSoup
# import json

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/dayco-kpt218#compatibility'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# # mencari elemen HTML dengan class "compatibility-container"
# am_comp = soup.find('div', {'class': 'compatibility-container'})

# # mencari semua elemen tabel di dalam elemen HTML dengan class "ausct"
# tables = am_comp.find_all('table', class_='ausct')

# # membuat dictionary kosong untuk menyimpan hasil
# result = {}

# # mengambil teks dalam tabel dan menyimpannya dalam dictionary
# for table in tables:
#     brand = ''
#     model = ''
#     modelYears = ''
#     spec_name = ''
#     spec_value = ''
#     rows = table.find_all('tr')
#     for row in rows:
#         if 'class' in row.attrs and 'ausctmh' in row['class']:
#             brand = row.find('td', {'class': 'acc-head'}).text.strip()
#         elif 'class' in row.attrs and 'ausctsh' in row['class']:
#             model = row.find('td', {'class': 'acc-head'}).text.strip()
#             if brand not in result:
#                 result[brand] = {}
#             if model not in result[brand]:
#                 result[brand][model] = {}
#         elif 'class' in row.attrs and 'ausctsh' in row['class']:
#             modelYears = row.find('td', {'class': 'acc-head'}).text.strip()
#             if model not in result:
#                 result[model] = {}
#             if modelYears not in result[model]:
#                 result[brand][model][modelYears] = {}
#         elif 'class' in row.attrs and 'ausctlh' in row['class']:
#             spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
#             spec_value = ''
#         elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
#             spec_container = row.find('td')
#             spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
#             spec_value = ':'.join(spec_value_parts)
#             result[brand][model][spec_name] = spec_value

# # mengubah hasil menjadi format json dan menampilkan
# list_of_vehicle_compatibility = json.dumps(result, indent=4)
# print(list_of_vehicle_compatibility)



# import requests
# from bs4 import BeautifulSoup
# import json

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/dayco-kpt218#compatibility'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# # mencari elemen HTML dengan class "compatibility-container"
# am_comp = soup.find('div', {'class': 'compatibility-container'})

# # mencari semua elemen tabel di dalam elemen HTML dengan class "ausct"
# tables = am_comp.find_all('table', class_='ausct')

# # membuat dictionary kosong untuk menyimpan hasil
# result = {}

# # mengambil teks dalam tabel dan menyimpannya dalam dictionary
# for table in tables:
#     brand = ''
#     model = ''
#     modelYears = ''
#     spec_name = ''
#     spec_value = ''
#     rows = table.find_all('tr')
#     for row in rows:
#         if 'class' in row.attrs and 'ausctmh' in row['class']:
#             brand = row.find('td', {'class': 'acc-head'}).text.strip()
#         elif 'class' in row.attrs and 'ausctsh' in row['class']:
#             model = row.find('td', {'class': 'acc-head'}).text.strip()
#             if brand not in result:
#                 result[brand] = {}
#             if model not in result[brand]:
#                 result[brand][model] = {}
#                 # print(result)
#             if model not in result[brand][model]:
#                 result[brand][model][modelYears] = {}
#             elif 'class' in row.attrs and 'ausctlh' in row['class']:
#                 spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
#                 spec_value = ''
#             elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
#                 spec_container = row.find('td')
#                 spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
#                 spec_value = '"' .join(spec_value_parts)
#                 spec_value = spec_value 
#                 result[brand][model][modelYears][spec_name] = spec_value.replace(':,',':')
                
      

# # mengubah hasil menjadi format json dan menampilkan
# list_of_vehicle_compatibility = json.dumps(result, indent=4)
# print(list_of_vehicle_compatibility)



# import requests
# from bs4 import BeautifulSoup
# import json

# data = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/dayco-kpt218#compatibility'
# r = requests.get(url)

# # membuat objek BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')

# # mencari elemen HTML dengan class "compatibility-container"
# am_comp = soup.find('div', {'class': 'compatibility-container'})

# # mencari semua elemen tabel di dalam elemen HTML dengan class "ausct"
# tables = am_comp.find_all('table', class_='ausct')

# # membuat dictionary kosong untuk menyimpan hasil
# result = {}

# # mengambil teks dalam tabel dan menyimpannya dalam dictionary
# for table in tables:
#     brand = ''
#     model = ''
#     modelYears = ''
#     spec_name = ''
#     spec_value = ''
#     rows = table.find_all('tr')
#     for row in rows:
#         if 'class' in row.attrs and 'ausctmh' in row['class']:
#             brand = row.find('td', {'class': 'acc-head'}).text.strip()
#         elif 'class' in row.attrs and 'ausctmh-container' in row['class']:
#             model = row.find('td', {'class': 'acc-head'}).text.strip()
#             if brand not in result:
#                 result[brand] = {}
#             if model not in result[brand]:
#                 result[brand][model] = {}


#             if modelYears not in result[brand]:
#                 result[brand][model][modelYears] = {}
#                 # print(modelYears)
#         elif 'class' in row.attrs and 'ausctlh' in row['class']:
#             spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
#             spec_value = ''
#         elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
#             spec_container = row.find('td')
#             spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
#             spec_value = ':'.join(spec_value_parts)
#             result[brand][model][modelYears][spec_name] = spec_value

# # mengubah hasil menjadi format json dan menampilkan
# list_of_vehicle_compatibility = json.dumps(result, indent=4)
# print(list_of_vehicle_compatibility)



import requests
from bs4 import BeautifulSoup
import json

data = []

# membuat permintaan ke URL
url = 'https://automotivesuperstore.com.au/dayco-kpt218#compatibility'
r = requests.get(url)

# membuat objek BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

# mencari elemen HTML dengan class "compatibility-container"
am_comp = soup.find('div', {'class': 'compatibility-container'})

# mencari semua elemen tabel di dalam elemen HTML dengan class "ausct"
tables = am_comp.find_all('table', class_='ausct')

# membuat dictionary kosong untuk menyimpan hasil
result = {}

# mengambil teks dalam tabel dan menyimpannya dalam dictionary
for table in tables:
    brand = ''
    model = ''
    modelYears = ''
    spec_name = ''
    spec_value = ''
    rows = table.find_all('tr')
    for row in rows:
        if 'class' in row.attrs and 'ausctmh' in row['class']:
            brand = row.find('td', {'class': 'acc-head'}).text.strip()
            # modelYears = ''
        elif 'class' in row.attrs and 'ausctmh-container' in row['class']:
            model = row.find('td', {'class': 'acc-head'}).text.strip()
            if brand not in result:
                result[brand] = {}
            if model not in result[brand]:
                result[brand][model] = {}

        elif 'class' in row.attrs and 'ausctlh' in row['class']:
            modelYears = row.find('td', {'class': 'acc-head'}).text.strip()
            if spec_name not in result[brand][model]:
                result[brand][model][modelYears] = {}

        elif 'class' in row.attrs and 'ausctlh' in row['class']:
            spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
            spec_value = ''
        elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
            spec_container = row.find('td')
            spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
            spec_value = ':'.join(spec_value_parts)
            result[brand][model][modelYears][spec_name] = spec_value

# # mengubah hasil menjadi format json dan menampilkan
list_of_vehicle_compatibility = json.dumps(result, indent=4)
print(list_of_vehicle_compatibility)
