# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# baseurl = 'https://automotivesuperstore.com.au'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# categorylinks = []
# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')
# categorylist = soup.find_all('div', {'data-content-type': 'button-item', 'data-appearance': 'default', 'data-element': 'main'})
# for itemcategorylist in categorylist:
#     for linkcategory in itemcategorylist.find_all('a', class_='pagebuilder-button-link', href=True):
#         categorylinks.append(linkcategory['href'])

# data = []
# processed_urls = set()

# for linkcategory in categorylinks:
#     r = requests.get(linkcategory, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')
#     textlint = soup.find('h1', class_='page-title').text
#     print(textlint)
#     try:
#         productItem = soup.find_all('ul', class_='subcategories service-catlist')
#     except:
#         continue
#     for item in productItem:
#         productList = []
#         for href in item.find_all('a', class_='category-image', href=True):
#             url = href['href']
#             if url not in processed_urls:
#                 productList.append(url)
#                 processed_urls.add(url)

#         for linkproduct in productList:
#             r = requests.get(linkproduct, headers=headers)
#             soup = BeautifulSoup(r.content, 'lxml')
#             lintpro = soup.find('h1', class_='page-title').text
#             print(lintpro)
#             try:
#                 itemproductlinks = soup.find_all('ul', class_='subcategories service-catlist')
#             except:
#                 continue
#             for itemlinks in itemproductlinks:
#                 productlinks = []
#                 for hrefitem in itemlinks.find_all('a', class_='category-image', href=True):
#                     url = hrefitem['href']
#                     if url not in processed_urls:
#                         productlinks.append(url)
#                         processed_urls.add(url)
                
#                 for itemlinkproduct in processed_urls:
#                     for linkCategoryProduct in itemlinkproduct.find_all('a', class_='product photo product-item-photo',href=True):
#                         print(linkCategoryProduct)



import requests
from bs4 import BeautifulSoup
import csv
import json

baseurl = 'https://automotivesuperstore.com.au'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

processed_urls = set() # definisikan variabel processed_urls di sini

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
                        r = requests.get(url, headers=headers) # buat permintaan HTTP untuk halaman baru
                        soup = BeautifulSoup(r.content, 'lxml')
                        for linkCategoryProduct in soup.find_all('a', class_='product photo product-item-photo', href=True):
                            print(linkCategoryProduct['href'])
