# import requests
# from bs4 import BeautifulSoup
# import csv
# import json
# import time

# baseurl = 'https://www.hardrace.co.uk/vehicle-search-new.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
# }

# data = []

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# processed_urls = set()

# produclinks = []

# aplicarionNameCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

# for catrList in aplicarionNameCars:
#     for link in catrList.find_all('a', href=True):
#         url = link['href']
#         if url not in processed_urls:
#             produclinks.append(url)
#             processed_urls.add(url)
# # print(len(produclinks))

# for make_name_url in produclinks:
#     r = requests.get(make_name_url, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
#     make_name = soup.find('h1', class_='page-title').text.strip()
#     print(make_name_url, make_name)

#     productItemLinks = []
#     for product_item in listItemCars:
#         for link_product_item in product_item.find_all('a', href=True):
#             urlproduct = link_product_item['href']
#             if urlproduct not in processed_urls:
#                 productItemLinks.append(urlproduct)
#                 processed_urls.add(urlproduct)

#     for modelUrlName in productItemLinks:
#         r = requests.get(modelUrlName, headers=headers)
#         soup = BeautifulSoup(r.content, 'lxml')
#         model_name = soup.find('h1', class_='page-title').text.strip()

#         # result = []

#         # result.append({
#         #     "make": make_name,
#         #     "model": model_name,
#         #     "type": ''
#         # })
#         # list_of_Vehicle_Compatibility = json.dumps(result)

#         try:
#             product_items_no_type = soup.find_all('strong', class_='product-item-name')
#             product_items_type = []  # Tambahkan inisialisasi variabel product_items_type
#         except:
#             None

#         linktypeUrl = []
#         listTypeModel = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

#         for ListTypeUrl in listTypeModel:
#             for typeUrl in ListTypeUrl.find_all('a', class_='mt-auto', href=True):
#                 texttypeUrl = typeUrl.text.strip()
#                 linktypeUrl.append((typeUrl['href'], texttypeUrl))

#         for urltype, texttypeUrl in linktypeUrl:
#             r = requests.get(urltype, headers=headers)
#             soup = BeautifulSoup(r.content, 'lxml')

#             product_items_type = soup.find_all('strong', class_='product-item-name')

#         urlPageModel = product_items_no_type + product_items_type

#         print(urlPageModel)


# import requests
# from bs4 import BeautifulSoup
# import csv
# import json
# import time

# baseurl = 'https://www.hardrace.co.uk/vehicle-search-new.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
# }

# data = []

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# processed_urls = set()

# produclinks = []

# aplicarionNameCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

# for catrList in aplicarionNameCars:
#     for link in catrList.find_all('a', href=True):
#         url = link['href']
#         if url not in processed_urls:
#             produclinks.append(url)
#             processed_urls.add(url)
# # print(len(produclinks))

# for make_name_url in produclinks:
#     r = requests.get(make_name_url, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
#     make_name = soup.find('h1', class_='page-title').text.strip()
#     print(make_name_url, make_name)

#     productItemLinks = []
#     for product_item in listItemCars:
#         for link_product_item in product_item.find_all('a', href=True):
#             urlproduct = link_product_item['href']
#             if urlproduct not in processed_urls:
#                 productItemLinks.append(urlproduct)
#                 processed_urls.add(urlproduct)

#     for modelUrlName in productItemLinks:
#         r = requests.get(modelUrlName, headers=headers)
#         soup = BeautifulSoup(r.content, 'lxml')
#         model_name = soup.find('h1', class_='page-title').text.strip()

#         try:
#             product_items_no_type = soup.find_all('strong', class_='product-item-name')
#             product_items_type = []  # Tambahkan inisialisasi variabel product_items_type
#         except:
#             None

#         listTypeModel = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

#         for ListTypeUrl in listTypeModel:
#             linktypeUrl = []
#             for typeUrl in ListTypeUrl.find_all('a', class_='mt-auto', href=True):
#                 texttypeUrl = typeUrl.text.strip()
#                 linktypeUrl.append((typeUrl['href'], texttypeUrl))

#             for urltype, texttypeUrl in linktypeUrl:
#                 r = requests.get(urltype, headers=headers)
#                 soup = BeautifulSoup(r.content, 'lxml')

#                 # product_items_type = soup.find_all('strong', class_='product-item-name')

#                 urlPageModel = product_items_no_type + product_items_type

#         print(product_items_no_type,urltype, texttypeUrl)



# import requests
# from bs4 import BeautifulSoup
# import csv
# import json
# import time

# baseurl = 'https://www.hardrace.co.uk/vehicle-search-new.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
# }

# data = []

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# processed_urls = set()

# produclinks = []

# aplicarionNameCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

# for catrList in aplicarionNameCars:
#     for link in catrList.find_all('a', href=True):
#         url = link['href']
#         if url not in processed_urls:
#             produclinks.append(url)
#             processed_urls.add(url)
# # print(len(produclinks))

# for make_name_url in produclinks:
#     r = requests.get(make_name_url, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
#     make_name = soup.find('h1', class_='page-title').text.strip()
#     print(make_name_url, make_name)

#     productItemLinks = []
#     for product_item in listItemCars:
#         for link_product_item in product_item.find_all('a', href=True):
#             urlproduct = link_product_item['href']
#             if urlproduct not in processed_urls:
#                 productItemLinks.append(urlproduct)
#                 processed_urls.add(urlproduct)

#     for modelUrlName in productItemLinks:
#         r = requests.get(modelUrlName, headers=headers)
#         soup = BeautifulSoup(r.content, 'lxml')
#         model_name = soup.find('h1', class_='page-title').text.strip()

#         print(model_name, modelUrlName)

#         linktypeUrl = []
#         listTypeModel = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

#         for ListTypeUrl in listTypeModel:
#             for typeUrl in ListTypeUrl.find_all('a', class_='mt-auto', href=True):
#                 texttypeUrl = typeUrl.text.strip()
#                 linktypeUrl.append((typeUrl['href'], texttypeUrl))

#         for urltype, texttypeUrl in linktypeUrl:
#             page_num = 1
#             while True:
#                 page_url = urltype + f'?p={page_num}'
#                 r = requests.get(page_url, headers=headers)
#                 soup = BeautifulSoup(r.content, 'lxml')

#                 print(page_url, texttypeUrl)

#                 product_items = soup.find_all('strong', class_='product-item-name')
#                 for product_item in product_items:
#                     productItem = product_item.find('a', class_='product-item-link', href=True)
#                     if productItem:
#                         link = productItem['href']
                                
#                         r = requests.get(link, headers=headers)
#                         soup = BeautifulSoup(r.content, 'lxml')

#                         productTitle = soup.find('h1', class_='page-title').text.strip()
#                         print(productTitle)
#                 page_num += 1

#         # except:
#         #     None

#                 # product_items_type = soup.find_all('strong', class_='product-item-name')

#                 # urlPageModel = product_items_no_type + product_items_type

#                 # print(product_items_no_type, urltype, texttypeUrl)

#         # print(product_items_no_type, urltype, texttypeUrl)


import requests
from bs4 import BeautifulSoup
import csv
import json
import time

baseurl = 'https://www.hardrace.co.uk/vehicle-search-new.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

processed_urls = set()

produclinks = []

aplicarionNameCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

for catrList in aplicarionNameCars:
    for link in catrList.find_all('a', href=True):
        url = link['href']
        if url not in processed_urls:
            produclinks.append(url)
            processed_urls.add(url)

for make_name_url in produclinks:
    r = requests.get(make_name_url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
    make_name = soup.find('h1', class_='page-title').text.strip()
    print(make_name_url, make_name)

    productItemLinks = []
    for product_item in listItemCars:
        for link_product_item in product_item.find_all('a', href=True):
            urlproduct = link_product_item['href']
            if urlproduct not in processed_urls:
                productItemLinks.append(urlproduct)
                processed_urls.add(urlproduct)

    for modelUrlName in productItemLinks:
        r = requests.get(modelUrlName, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        model_name = soup.find('h1', class_='page-title').text.strip()

        print(model_name, modelUrlName)

        linktypeUrl = []
        listTypeModel = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

        for ListTypeUrl in listTypeModel:
            for typeUrl in ListTypeUrl.find_all('a', class_='mt-auto', href=True):
                texttypeUrl = typeUrl.text.strip()
                linktypeUrl.append((typeUrl['href'], texttypeUrl))


        for typeUrl, texttypeUrl in linktypeUrl:
            page_num = 1
            while True:
                page_url = typeUrl + f'?p={page_num}'

                r = requests.get(page_url, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')

                print(typeUrl, texttypeUrl)

                product_items = soup.find_all('strong', class_='product-item-name')
                if not product_items:
                    break
                for product_item in product_items:
                    productItem = product_item.find('a', class_='product-item-link', href=True)
                    if productItem:
                        link = productItem['href']
                    
                        r = requests.get(link, headers=headers)
                        soup = BeautifulSoup(r.content, 'lxml')

                        productTitle = soup.find('h1', class_='page-title').text.strip()
                        print(productTitle)
                page_num += 1

        product_items = soup.find_all('strong', class_='product-item-name')
        if not product_items:
            break
        for product_item in product_items:
            productItem = product_item.find('a', class_='product-item-link', href=True)
            if productItem:
                link = productItem['href']
                    
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')

                productTitle = soup.find('h1', class_='page-title').text.strip()
                print(productTitle)
