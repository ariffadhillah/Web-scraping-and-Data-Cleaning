import requests
from bs4 import BeautifulSoup
import json
import csv

data = []
dataresult = []
dataresultOther_fitment = []
# membuat permintaan ke URL
url = 'https://automotivesuperstore.com.au/aeroflow-af463-0032b'
r = requests.get(url)

# membuat objek BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others', 'Other_fitment']
filename = 'automotivesuperstoretest.csv'


part_number_element = soup.find('div', class_='product attribute partnumber')
if part_number_element:
    try:
        PartNumber = part_number_element.text.replace('Part No.', '').strip()    
    except:
        PartNumber = ''
else:
    print(' ')

try:
    productTitle = soup.find('h1', class_='page-title').text.strip()    
except:
    productTitle = ''

try:
    productDescription = soup.find('div', class_='product attribute description').text.strip()    
except:
    productDescription = ''

# gallery-placeholder

try:
    imgproductmedia = soup.find('div', {'class': 'product media'})
    image = imgproductmedia.find('img', {'class': 'gallery-placeholder__image'})
    image_url = image['src']
except:
    image_url = ''

try:
    price_wrapper = soup.find('span', {'data-price-type': 'finalPrice'})
    price = price_wrapper.find('span', {'class': 'price'}).text
except:
    price = ''


#/ Compatibility  the pure vehicle info json
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
    list_of_vehicle_compatibility = json.dumps(dataresult)
    # print(json.dumps(dataresult, indent=2))
except:
    list_of_vehicle_compatibility = ' '



#/ Compatibility Other_fitment json
try:
    divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

    tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')
   
    for table_Other_fitment in tables_Other_fitment:
        
        trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')
        
        for trOther in trOther_fitment:
            fitment_data = {}
            Otherfitment = trOther.find_all('td')
            
            for fitment in Otherfitment:
              
                Otherfitment_text = fitment.get_text(strip=True)
                if ':' in Otherfitment_text:
                    key, value = Otherfitment_text.split(':', 1)
                    fitment_data[key] = value
                else:
                    fitment_data['Positions'] = Otherfitment_text
                
            dataresultOther_fitment.append(fitment_data)
    
    Other_fitment = json.dumps(dataresultOther_fitment)
              
except:
    Other_fitment = ''


# Specifications / Others
try:
    spec_group = soup.find('div', {'class': 'spec-group'})
    rows = spec_group.find_all('tr')
    specs = {}
    for row in rows:
        key = row.find('th').text.strip().replace(':', '')
        value = row.find('td').text.strip()
        specs[key] = value
    others = json.dumps(specs)
except:
    others = ''


try:
    product_info_main = soup.find('div', {'class': 'product-info-main'})
    altimage = product_info_main.find('img')
    brand = altimage.get('alt')
    
except:
    brand = ''

Automotivesuperstore = {
    'Category (Parent)': '',
    'Category URL (Parent)': '',
    'Category - Leaf (Child 1)': '',
    'Category URL - Leaf (Child 1)': '',
    'Product URL': '',
    'PartNumber': PartNumber,
    'Product Title': productTitle, 
    'Product Subtitle': '',
    'Product Description': productDescription,
    'Image URLs': image_url,
    'Price': price,
    'List of Vehicle Compatibility': list_of_vehicle_compatibility,
    'Brand': brand,
    'OE number / cross-reference': '',
    'Others': others,
    'Other_fitment': Other_fitment.replace('To ~','","To":"').replace('Quantity Per Vehicle:','","Quantity Per Vehicle":"').replace('Product Fitment Note:','","Product Fitment Note":"').replace('": "','":"').replace('Catalog Type:Roll Control','","Catalog Type:Roll Control').replace('Fitment Retail:','","Fitment Retail":"').replace('PAFootNote1:','","PAFootNote1":"').replace('Catalog Type:', 'Catalog Type":"').replace('Catalog Type','","Catalog Type').replace('"",','').replace('PAFootNote2:','","PAFootNote2":"').replace('PAFootNote3:','","PAFootNote3":"').replace('Outcome:','","Outcome":"'),
}

data.append(Automotivesuperstore)
print('Saving', Automotivesuperstore['Brand'])

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print('Data is successfully saved in the file', filename)




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



# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')


# #/ Compatibility  the pure vehicle info json
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
#                 listothers = tr.find_next_sibling('tr')
#                 others_list = listothers.find_all('td', class_='acc-head')
#                 for others in others_list:
#                     others_text = others.text.strip()
#                     dataresult.append({"make": make, "model": model_text, "others": others_text})
#     list_of_vehicle_compatibility = json.dumps(dataresult)
#     # print(json.dumps(dataresult, indent=2))
# except:
#     list_of_vehicle_compatibility = ' '
# # print(list_of_vehicle_compatibility)



# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')



# #/ Compatibility Other_fitment json
# try:
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')
   
#     for table_Other_fitment in tables_Other_fitment:
#         # titlebrand1 = table_Other_fitment.find('tr', class_='ausctmh')
        
#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')
        
#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')
            
#             for fitment in Otherfitment:
              
#                 Other_fitment = fitment
#                 print(Other_fitment)
              
# except:
#     print(' None ')


# import requests
# from bs4 import BeautifulSoup
# import json

# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')

# dataresult = []

# divOther_fitment = soup.find('div', {'class': 'compatibility-container'})
# tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')

# for table_Other_fitment in tables_Other_fitment:
#     trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')
#     for trOther in trOther_fitment:
#         Otherfitment = trOther.find_all('td')
#         other_fitment_data = {}
#         for fitment in Otherfitment:
#             strong_tags = fitment.find_all('strong')
#             br_tags = fitment.find_all('br')
#             p_tags = fitment.find_all('p')
#             for tag in strong_tags:
#                 key = tag.text.strip()
#                 value = tag.find_next_sibling(text=True).strip()
#                 other_fitment_data[key] = value
#             for tag in br_tags:
#                 key = tag.previous_sibling.strip().replace(':', '')
#                 value = tag.next_sibling.strip()
#                 other_fitment_data[key] = value
#             for tag in p_tags:
#                 key = tag.find('b').text.strip().replace(':', '')
#                 value = tag.find('span').text.strip()
#                 other_fitment_data[key] = value
#         dataresult.append(other_fitment_data)

# print(json.dumps(dataresult))



# import requests
# from bs4 import BeautifulSoup

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# dataresult = []

# # Compatibility Other_fitment json
# try:
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})
#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')

#     for table_Other_fitment in tables_Other_fitment:
#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')

#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')

#             for fitment in Otherfitment:
#                 # membuat dictionary baru
#                 fitment_dict = {}

#                 # mendapatkan teks pada setiap tag <strong>, <br>, dan <p>
#                 for tag in fitment.find_all(['strong', 'br', 'p']):
#                     key = tag.text.strip().replace(':', '')
#                     value = tag.next_sibling.strip() if tag.next_sibling is not None else ""
#                     fitment_dict[key] = value

#                     dataresult.append(fitment_dict)
#                     print(dataresult)
# except:
#     print('None')

# # print(dataresult)



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
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')

#     for table_Other_fitment in tables_Other_fitment:
#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')
#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')

#             # dictionary untuk menyimpan hasil ekstraksi
#             extracted_data = {}

#             # loop pada setiap elemen <td>
#             for fitment in Otherfitment:
#                 print(Otherfitment)
#                 # mencari tag <strong> dan <br> di dalam elemen <td>
#                 strong_tags = fitment.find_all('strong')
#                 br_tags = fitment.find_all('br')
#                 p_tags = fitment.find_all('p')

#                 # menyimpan teks di antara tag <strong> dan <br> ke dalam dictionary
#                 for i in range(len(strong_tags)):
#                     if i < len(br_tags):
#                         key = strong_tags[i].text.strip()
#                         value = br_tags[i].next_sibling.strip()
#                         extracted_data[key] = value

#                 # menyimpan teks di antara tag <p> ke dalam dictionary
#                 for p_tag in p_tags:
#                     key = p_tag.text.strip()
#                     value = p_tag.next_sibling.strip()
#                     extracted_data[key] = value

#             # menambahkan dictionary hasil ekstraksi ke dalam list
#             dataresult.append(extracted_data)

# except:
#     print(' None ')

# # mencetak hasil ekstraksi ke dalam format JSON
# # print(json.dumps(dataresult, indent=4))



# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# #/ Compatibility Other_fitment json
# try:
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')
   
#     for table_Other_fitment in tables_Other_fitment:
#         # titlebrand1 = table_Other_fitment.find('tr', class_='ausctmh')
        
#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')
        
#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')
            
#             # loop pada setiap elemen <td>
#             for fitment in Otherfitment:
#                 strong_tags = fitment.find_all('strong')
  
                
                

# except:
#     print(' None ')


# import requests
# from bs4 import BeautifulSoup
# import json

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# #/ Compatibility Other_fitment json
# try:
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')

#     for table_Other_fitment in tables_Other_fitment:
#         # titlebrand1 = table_Other_fitment.find('tr', class_='ausctmh')

#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')

#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')

#             # loop pada setiap elemen <td>
#             for fitment in Otherfitment:
#                 strong_tags = fitment.find_all('strong')
#                 fitment_dict = {}
#                 for tag in strong_tags:
#                     tag_text = tag.get_text(strip=True)
#                     next_element = tag.next_sibling.strip()
#                     fitment_dict[tag_text] = next_element
#                 dataresult.append(fitment_dict)

#                 # menampilkan hasil
#                 print(fitment_dict)

# except:
#     print(' None ')



# # dump dataresult ke json
# with open('test.json', 'w') as f:
#     json.dump(dataresult, f, indent=2)




# import requests
# from bs4 import BeautifulSoup
# import json

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')

# #/ Compatibility Other_fitment json
# try:
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')

#     for table_Other_fitment in tables_Other_fitment:
#         # titlebrand1 = table_Other_fitment.find('tr', class_='ausctmh')

#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')

#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')

#             # loop pada setiap elemen <td>
#             for fitment in Otherfitment:
#                 strong_tags = fitment.find_all('strong')
#                 fitment_dict = {}
#                 for tag in strong_tags:
#                     tag_text = tag.get_text(strip=True)
#                     next_element = tag.next_sibling.strip() if tag.next_sibling is not None else ""
#                     fitment_dict[tag_text] = next_element
#                     if next_element:
#                         print(f"{tag_text}{next_element}")
#                 remaining_text = fitment.get_text(strip=True)
#                 if remaining_text and remaining_text not in fitment_dict.values():
#                     print(f"{remaining_text}")
#                 dataresult.append(fitment_dict)

# except:
#     print(' None ')


# import requests
# from bs4 import BeautifulSoup
# import json

# dataresult = []

# # membuat permintaan ke URL
# url = 'https://automotivesuperstore.com.au/afi-dra1001'
# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')


# #/ Compatibility  the pure vehicle info json
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
#                 listothers = tr.find_next_sibling('tr')
#                 others_list = listothers.find_all('td', class_='acc-head')
#                 for others in others_list:
#                     others_text = others.text.strip()
#                     dataresult.append({"make": make, "model": model_text, "others": others_text})
#     list_of_vehicle_compatibility = json.dumps(dataresult)
#     # print(json.dumps(dataresult, indent=2))
# except:
#     list_of_vehicle_compatibility = ' '


# #/ Compatibility Other_fitment json
# try:
#     divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

#     tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')

#     for table_Other_fitment in tables_Other_fitment:
#         # titlebrand1 = table_Other_fitment.find('tr', class_='ausctmh')

#         trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')

#         for trOther in trOther_fitment:
#             Otherfitment = trOther.find_all('td')

#             # loop pada setiap elemen <td>
#             fitment_dict = {}
#             for fitment in Otherfitment:
#                 strong_tags = fitment.find_all('strong')
#                 for tag in strong_tags:
#                     tag_text = tag.get_text(strip=True)
#                     next_element = tag.next_sibling.strip() if tag.next_sibling is not None else ""
#                     fitment_dict[tag_text] = next_element
#                 remaining_text = fitment.get_text(strip=True)
#                 if remaining_text and remaining_text not in fitment_dict.values():
#                     fitment_dict[""] = remaining_text

#             dataresult.append(fitment_dict)

#     # mengkonversi hasil ke dalam format JSON dan menampilkan
#     json_result = json.dumps(dataresult, indent=4)

# except:
#     print(' None ')
