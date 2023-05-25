# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# # import json
# # import time
# # import time


# # baseurl ='https://www.hardrace.co.uk/vehicle-search-new/alfa.html'
# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
# # }

# # r = requests.get(baseurl, headers=headers)

# # processed_urls = set() 

# # produclinks = []
# # soup = BeautifulSoup(r.content, 'lxml')

# # productItemLinks = []
# # listItemCars = soup.find_all('div', class_='h-100 d-flex flex-column')
# # for product_item in listItemCars:
# #     for link_product_item in product_item.find_all('a', href=True):
# #         urlproduct = link_product_item['href']
# #         if urlproduct not in processed_urls:
# #             productItemLinks.append(urlproduct)
# #             processed_urls.add(urlproduct)  

# # for itemCars in productItemLinks:
# #     time.sleep(.3)
# #     r = requests.get(itemCars, headers=headers)
# #     soup = BeautifulSoup(r.content, 'lxml')

# #     pageList = []
# #     titleCarsCategory = soup.find('h1', class_='page-title').text.strip()
# #     lenitemproduct = soup.find('p', id='toolbar-amount').text.strip()
# #     naemListProduct = soup.find('h1', id='page-title-heading').text.strip()

# #     print(itemCars, lenitemproduct, naemListProduct)

# #     time.sleep(.3)
# #     product_items = soup.find_all('strong', class_='product name product-item-name')

# #     for product_item in product_items:
# #         productitemlink = product_item.find('a', class_='product-item-link', href=True)
# #         if productitemlink:
# #             pageitemLink = productitemlink['href']
# #             if pageitemLink not in processed_urls:
# #                 pageList.append(pageitemLink)
# #                 processed_urls.add(pageitemLink)
# #     print(pageList)




# import requests
# from bs4 import BeautifulSoup
# import time

# baseurl ='https://www.hardrace.co.uk/vehicle-search-new/alfa.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
# }

# r = requests.get(baseurl, headers=headers)

# processed_urls = set() 

# produclinks = []
# soup = BeautifulSoup(r.content, 'lxml')

# productItemLinks = []
# listItemCars = soup.find_all('div', class_='h-100 d-flex flex-column')
# for product_item in listItemCars:
#     for link_product_item in product_item.find_all('a', href=True):
#         urlproduct = link_product_item['href']
#         if urlproduct not in processed_urls:
#             productItemLinks.append(urlproduct)
#             processed_urls.add(urlproduct)  

# for itemCars in productItemLinks:
#     time.sleep(.3)
#     r = requests.get(itemCars, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     pageList = []
#     titleCarsCategory = soup.find('h1', class_='page-title').text.strip()
#     lenitemproduct = soup.find('p', id='toolbar-amount').text.strip()
#     naemListProduct = soup.find('h1', id='page-title-heading').text.strip()

#     print(itemCars, lenitemproduct, naemListProduct)

#     time.sleep(.3)
#     product_items = soup.find_all('strong', class_='product name product-item-name')
#     for product_item in product_items:
#         link = product_item.find('a', class_='product-item-link')['href']
#         print(link)
#         print(product_item.text.strip())





import requests
from bs4 import BeautifulSoup
import time

baseurl ='https://www.hardrace.co.uk/vehicle-search-new/alfa.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}

r = requests.get(baseurl, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

productItemLinks = []
listItemCars = soup.find_all('div', class_='h-100 d-flex flex-column')
for product_item in listItemCars:
    for link_product_item in product_item.find_all('a', href=True):
        urlproduct = link_product_item['href']
        productItemLinks.append(urlproduct)

for typeUrlName in productItemLinks:
    r = requests.get(typeUrlName, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    type_name = soup.find('h1', id='page-title-heading').text.strip()
    print(typeUrlName, type_name)

    product_items = soup.find_all('strong', class_='product-item-name')

    for product_item in product_items:
        productItem = product_item.find('a', class_='product-item-link', href=True)
        if productItem:
            link = productItem['href']
            r = requests.get(link, headers=headers)
            soup_product = BeautifulSoup(r.content, 'lxml')
            productTitle = soup_product.find('h1', class_='page-title').text.strip()
            sku = soup_product.find('div', class_='product attribute sku').text.strip().replace('SKU', '')
            price = soup_product.find('span', class_='price-wrapper price-including-tax').text.strip()
            detailS = soup_product.find('div', class_='product attribute description').text.strip()
            productSubtitle = soup_product.find('td', {'data-th':'Subtitle'}, class_='col data' ).text.strip()

            # product_attribute_overview = soup_product.find('div', class_='product attribute overview')
            # if product_attribute_overview:
            #     product_attribute_overview_text = product_attribute_overview.text.strip()
            #     print(product_attribute_overview_text)
            # else:
            #     print("Product attribute overview not found")

            # product_attribute_overview = soup.find('div', class_='product attribute overview').text.strip()
            
            # hardraceProductPromo = soup.find('div', class_='hardraceProductPromo').find('ul').text.strip()
            # print(product_attribute_overview_text)
            print(productTitle, sku, price, detailS, productSubtitle)
                