# import requests
# from bs4 import BeautifulSoup
# import csv
# import json
# import time

# baseurl = 'https://automotivesuperstore.com.au/service/vehicle-service-kits/audi-service-kits'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# processed_urls = set() 
# data = []

# url_Category_URL_Leaf_Child1 = baseurl['href']
# if url_Category_URL_Leaf_Child1 not in processed_urls:
#     processed_urls.add(url_Category_URL_Leaf_Child1)
#     print(url_Category_URL_Leaf_Child1)
#     page_num = 1
#     while True:
#         page_url = url_Category_URL_Leaf_Child1 + f'?p={page_num}'
#         r = requests.get(page_url, headers=headers)
#         soup = BeautifulSoup(r.content, 'lxml')
#         linkCategoryProducts = soup.find_all('a', class_='product photo product-item-photo', href=True)
#         if not linkCategoryProducts:
#             break
#         for linkCategoryProduct in linkCategoryProducts:
#             if linkCategoryProduct['href'] not in processed_urls:
#                 r = requests.get(linkCategoryProduct['href'] , headers=headers)
#                 soup = BeautifulSoup(r.content, 'lxml')
#                 dataresultcompatibility = []
#                 dataresultOther_fitment = []
#                 part_number_element = soup.find('div', class_='product attribute partnumber')
#                 if part_number_element:
#                     try:
#                         PartNumber = part_number_element.text.replace('Part No.', '').strip() 
#                     except:
#                         PartNumber = ''
#                 else:
#                     print(' ')
                    
#                     try:
#                         productTitle = soup.find('h1', class_='page-title').text.strip()    
#                     except:
#                         productTitle = ''
#         # print('Data is successfully saved in the file', filename)
#         page_num += 1
#         time.sleep(1) # time sleep





import requests
from bs4 import BeautifulSoup
import csv
import json
import time

baseurl = 'https://automotivesuperstore.com.au/service/vehicle-service-kits/audi-service-kits'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

processed_urls = set() 
data = []

fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others', 'Other_fitment']

filename = baseurl.split('/')[-1] + '.csv'


url_Category_URL_Leaf_Child1 = baseurl
if url_Category_URL_Leaf_Child1 not in processed_urls:
    processed_urls.add(url_Category_URL_Leaf_Child1)
    print(url_Category_URL_Leaf_Child1)
    page_num = 1
    while True:
        page_url = url_Category_URL_Leaf_Child1 + f'?p={page_num}'
        r = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        linkCategoryProducts = soup.find_all('a', class_='product photo product-item-photo', href=True)
        if not linkCategoryProducts:
            break
        for linkCategoryProduct in linkCategoryProducts:
            if linkCategoryProduct['href'] not in processed_urls:
                r = requests.get(linkCategoryProduct['href'] , headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')
                dataresultcompatibility = []
                dataresultOther_fitment = []
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
        
                Automotivesuperstore = {
                    'Category (Parent)': 'Home ' + baseurl.split('/')[-3].replace('-', ' ').title(),
                    'Category URL (Parent)': baseurl.split('/')[-4].replace('-', ' ').title(),
                    'Category - Leaf (Child 1)': ' '.join(Category_Leaf_Child).replace('\n', ' ').replace("['", "").replace("']",""),
                    'Category URL - Leaf (Child 1)': url_Category_URL_Leaf_Child1,
                    'Product URL': linkCategoryProduct['href'],
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
                print('Saving', Automotivesuperstore['PartNumber'],Automotivesuperstore['Category - Leaf (Child 1)'], Automotivesuperstore['Price'], Automotivesuperstore['Brand'], Automotivesuperstore['Product URL'], Automotivesuperstore['Others'])
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for item in data:
                        writer.writerow(item)
                
        page_num += 1
        time.sleep(1) # time sleep
