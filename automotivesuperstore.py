import requests
from bs4 import BeautifulSoup
import csv
import json
import time

baseurl = 'https://automotivesuperstore.com.au'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

processed_urls = set() 

categorylinks = []
r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
categorylist = soup.find_all('div', {'data-content-type': 'button-item', 'data-appearance': 'default', 'data-element': 'main'})
for itemcategorylist in categorylist:
    for linkcategory in itemcategorylist.find_all('a', class_='pagebuilder-button-link', href=True):
        categorylinks.append(linkcategory['href'])

data = []

for linkcategory in categorylinks:
    r = requests.get(linkcategory, headers=headers)
    print(linkcategory)
    soup = BeautifulSoup(r.content, 'lxml')
    textlint = soup.find('h1', class_='page-title').text
    print(textlint)
    try:
        productItem = soup.find_all('ul', class_='subcategories service-catlist')
    except:
        continue
    for item in productItem:
        productList = []
        for href in item.find_all('a', class_='category-image', href=True):
            url = href['href']
            if url not in processed_urls:
                productList.append(url)
                processed_urls.add(url)

        for linkproduct in productList:
            r = requests.get(linkproduct, headers=headers)
            print(linkproduct)
            soup = BeautifulSoup(r.content, 'lxml')
            lintpro = soup.find('h1', class_='page-title').text
            print(lintpro)
            try:
                itemproductlinks = soup.find_all('ul', class_='subcategories service-catlist')
            except:
                continue
            for itemlinks in itemproductlinks:
                for hrefitem in itemlinks.find_all('a', class_='category-image', href=True):
                    url = hrefitem['href']
                    if url not in processed_urls:
                        processed_urls.add(url)
                        print(url)
                        page_num = 1
                        while True:
                            page_url = url + f'?p={page_num}'
                            r = requests.get(page_url, headers=headers)
                            soup = BeautifulSoup(r.content, 'lxml')
                            linkCategoryProducts = soup.find_all('a', class_='product photo product-item-photo', href=True)
                            if not linkCategoryProducts:
                                break
                            for linkCategoryProduct in linkCategoryProducts:
                                print(linkCategoryProduct['href'])
                            page_num += 1
                            time.sleep(1) # time sleep
