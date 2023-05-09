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

produclist = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

for catrList in produclist:
    for link in catrList.find_all('a', href=True):
        url = link['href']
        if url not in processed_urls:
            produclinks.append(url)
            processed_urls.add(url)
# print(len(produclinks))
for listCarsCategory in produclinks:
    r = requests.get(listCarsCategory, headers=headers)
    print(listCarsCategory)
    soup = BeautifulSoup(r.content, 'lxml')
    
    try:
        titleCarsCategory = soup.find('h1', class_='page-title').text.strip()
        print(titleCarsCategory)
    except:
        titleCarsCategory = ''

    listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

    # print(listItemCars)
    
    productItemLinks = []
    for product_item in listItemCars:
        for link_product_item in product_item.find_all('a', href=True):
            urlproduct = link_product_item['href']
            if urlproduct not in processed_urls:
                productItemLinks.append(urlproduct)
                processed_urls.add(urlproduct)
    
    print(len(productItemLinks))

            
    for itemCars in productItemLinks:
        r = requests.get(itemCars, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        try:
            titleCarsCategory = soup.find('h1', class_='page-title').text.strip()      
            print(titleCarsCategory)  
        except:
            titleCarsCategory = ''
        
        


        try:
            listcars_itemcategory = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
            for itemsublink in listcars_itemcategory:
                urlItemproduct = []
                for sunitemcategory in itemsublink.find_all('a', href=True):
                    herfsunitem = sunitemcategory['href']
                    if herfsunitem not in processed_urls:
                        urlItemproduct.append(herfsunitem)
                        processed_urls.add(herfsunitem)
             
                # print(urlItemproduct)

                for linkitemproduct in urlItemproduct:
                    # linkitemproduct
                    r = requests.get(itemCars, headers=headers)
                    soup = BeautifulSoup(r.content, 'lxml')

                    try:
                        pageItemName = soup.find('h1', class_='page-title').text.strip()
                    except:
                        pageItemName = ''


                    pagelink = soup.find_all('li', class_='item product product-item' )
                    # print(pagelink)

                    # for linkproduct in pagelink:
                    #     pageProductLink = []
                    #     for hrefpage in linkproduct.find_all('a', href=True):
                    #         print(hrefpage['href'])
                        #     urlitem = hrefpage['href']
                        #     if urlitem not in processed_urls:
                        #         pageProductLink.append(urlitem)
                        #         processed_urls.add(urlitem)
                        # print('                                     ')
                        # print('-------------------------------------')
                        # print('                                     ')
                        # print(len(pageProductLink))
                        # print('-------------------------------------')
                        # print('                                     ')
                        # print(pageProductLink)
                        # print('                                     ')
                        # print('-------------------------------------')
                        # print('                                     ')
                        # print('                                     ')


                    

            


        except:
            continue
    
            # for itemsub in urlItemproduct
            
            # item_product = soup.find_all('li', class_='item product product-item') 
            # for item in item_product:
            #         print(item.find('a')['href'])

        
        # try:
        #     # item_product = soup.find_all('li', class_='item product product-item')
        #     # print(item_product['href'])
        #     item_product = soup.find_all('li', class_='item product product-item') 
        #     for item in item_product:
        #         print(item.find('a')['href'])

        #     # for pageLink in item_product:
        #     #     for linktest in pageLink.find_all('a', href=True):
        #     #         urlpage = link['href']
        #     #         print(urlpage)
        #             # if url not in processed_urls:
        #             #     produclinks.append(url)
        #             #     processed_urls.add(url)
        #     # print(item_product)
        #     # for itemProductLink in item_product.find_all('a', href=True):
        #     #     print(itemProductLink['href'])
        #     #     hrefproduct = itemProductLink['href']
        #     #     if hrefproduct not in processed_urls:
        #     #         pageProductLink.append(hrefproduct)
        #     #         processed_urls.add(hrefproduct)
        #     #         print(pageProductLink)
        # except:
        #     continue
        
        

            # listcars_itemcategory = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
            # for itemsublink in listcars_itemcategory:
            #     for sunitemcategory in itemsublink.find_all('a', href=True):
            #         print( '-------- utl sub -------')
            #         print( '   ')
            #         print(len(sunitemcategory['href'])) 
            #         print( '   ')
            
   


            
            # try:
            # except:
            #     continue
           
   

    # try:
    #     listItem_product = soup.find_all('li', class_='item product product-item')
    #     print(listItem_product)
    # except:
    #     listItem_product = ''



    
