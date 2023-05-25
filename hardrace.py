import requests
from bs4 import BeautifulSoup
import csv
import json
import time


baseurl ='https://www.hardrace.co.uk/vehicle-search-new.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}

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
# print(len(produclinks))
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

        model_name = soup.find('h1', id='page-title-heading').text.strip()
        print(modelUrlName, model_name)

        product_items = soup.find_all('strong', class_='product-item-name')

        for product_item in product_items:
            productItem = product_item.find('a', class_='product-item-link', href=True)
            if productItem:
                link = productItem['href']
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')
                productTitle = soup.find('h1', class_='page-title').text.strip()
                sku = soup.find('div', class_='product attribute sku').text.strip().replace('SKU', '')
                price = soup.find('span', class_='price-wrapper price-including-tax').text.strip()
                detailS = soup.find('div', class_='product attribute description').text.strip()
                productSubtitle = soup.find('td', {'data-th':'Subtitle'}, class_='col data' ).text.strip()

                discription_txt = soup.find('div', class_='product attribute overview').text.strip()
                discription_ul = soup.find('div', class_='hardraceProductPromo').text.strip()
                discription = discription_txt + 'br_row' + discription_ul  
                
                print(discription.replace('br_row', '\n'))
               


    # for itemCars in productItemLinks:

    #     r = requests.get(itemCars, headers=headers)
    #     soup = BeautifulSoup(r.content, 'lxml')
        
    #     titleCarsCategory = soup.find('h1', class_='page-title').text.strip()
    #     lenitemproduct = soup.find('p', id='toolbar-amount').text.strip()
    #     naemListProduct = soup.find('h1', id='page-title-heading').text.strip()
        
    #     print(itemCars, lenitemproduct, naemListProduct)   

    #     pageList = []        
    #     product_items = soup.find_all('li', class_='item product product-item')
    #     for product_Item in product_items:
    #         for hrefpageMenu in product_Item.find_all('a', href=True):
    #             pageitemLink = hrefpageMenu['href']
    #             if pageitemLink not in processed_urls:
    #                pageList.append(pageitemLink)
    #                processed_urls.add(pageitemLink) 
    #     print(pageList)
        
    #     productlinkItem = []
    #     try:
    #         itemsubCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
    #         for item in itemsubCars:
    #             listProduct = item.find('a', class_='mt-auto',  href=True)
    #             hrefitem = listProduct['href']
    #             if hrefitem not in processed_urls:
    #                 productlinkItem.append(hrefitem)
    #                 processed_urls.add(hrefitem)
            
    #         # print(productlinkItem)

    #         for productDetails in productlinkItem:
    #             r = requests.get(productDetails, headers=headers)
    #             soup = BeautifulSoup(r.content, 'lxml')

    #             # print('         ')                
    #             lenitemproduct = soup.find('p', id='toolbar-amount').text.strip()
    #             naemListProduct = soup.find('h1', id='page-title-heading').text.strip()
    #             print(productDetails, lenitemproduct, naemListProduct)
    #     except:
    #         continue
        
    # print(productDetails)
    # print(lenitemproduct)
    # print('         ')
    # print(naemListProduct)
    # print('         ')
    # print('........... end child ...........')
    # print('         ')
    # print('........... end product child ...........')
    # print('         ')



                
# import requests
# from bs4 import BeautifulSoup

# baseurl ='https://www.hardrace.co.uk/vehicle-search-new.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
# }

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

# for listCarsCategory in produclinks:
#     r = requests.get(listCarsCategory, headers=headers)
#     # print(listCarsCategory)
#     soup = BeautifulSoup(r.content, 'lxml')
#     titleCarsCategory = soup.find('h1', class_='page-title').text.strip()
    
#     productItemLinks = []
#     listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
#     for product_item in listItemCars:
#         for link_product_item in product_item.find_all('a', href=True):
#             urlproduct = link_product_item['href']
#             if urlproduct not in processed_urls:
#                 productItemLinks.append(urlproduct)
#                 processed_urls.add(urlproduct)   
#     # print(productItemLinks)     
            
#     # list_product_item_info = []
#     try:
#         for itemCars in productItemLinks:
#             r = requests.get(itemCars, headers=headers)
#             soup = BeautifulSoup(r.content, 'lxml')
#             titleCarsCategory = soup.find('h1', class_='page-title').text.strip()  
#             print(titleCarsCategory) 
#             # print(itemCars)

#             product_item_info_menu = soup.find_all('li', class_='item product product-item')
#             for pageProduct in product_item_info_menu:
#                 linkPageItem = []
#                 for linkPageProduct in pageProduct.find_all('a', href=True):
#                     urlPage = linkPageProduct['href']
#                     if urlPage not in processed_urls:
#                         linkPageItem.append(urlPage)
#                         processed_urls.add(urlPage)
#                 print(linkPageItem)
                
#     except:
#         continue
            

        
        
        # productlinkItem = []
        # try:
        #     itemsubCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
        #     for item in itemsubCars:
        #         listProduct = item.find('a', class_='mt-auto',  href=True)
        #         hrefitem = listProduct['href']
        #         if hrefitem not in processed_urls:
        #             productlinkItem.append(hrefitem)
        #             processed_urls.add(hrefitem)

        #     for productDetails in productlinkItem:
        #         r = requests.get(productDetails, headers=headers)
        #         soup = BeautifulSoup(r.content, 'lxml')
        #         product_item_info_subMenu = soup.find_all('div', class_='product-item-info')
        #         # print(product_item_info_subMenu)

        # except:
        #     continue






        # list_product_item_info.append(product_item_info_menu + product_item_info_subMenu)
        # print(list_product_item_info)


        # list_product_item_info = []
        # for itemCars in productItemLinks:
        #     r = requests.get(itemCars, headers=headers)
        #     soup = BeautifulSoup(r.content, 'lxml')
        #     titleCarsCategory = soup.find('h1', class_='page-title').text.strip()  
        #     print(titleCarsCategory) 

        #     product_item_info_menu = soup.find_all('li', class_='item product product-item')
        #     product_item_info_subMenu = [] 

        #     productlinkItem = []

        #     try:
        #         itemsubCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
        #         for item in itemsubCars:
        #             listProduct = item.find('a', class_='mt-auto',  href=True)
        #             hrefitem = listProduct['href']
        #             if hrefitem not in processed_urls:
        #                 productlinkItem.append(hrefitem)
        #                 processed_urls.add(hrefitem)

        #         for productDetails in productlinkItem:
        #             r = requests.get(productDetails, headers=headers)
        #             soup = BeautifulSoup(r.content, 'lxml')
        #             product_item_info_subMenu += soup.find_all('li', class_='item product product-item') 
        #             print(product_item_info_subMenu)

        #     except:
        #         continue

        #     # list_product_item_info.append(product_item_info_menu + product_item_info_subMenu)
        #     # print(list_product_item_info)

