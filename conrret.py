import requests
from bs4 import BeautifulSoup
import csv
import json

baseurl = 'https://automotivesuperstore.com.au'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

categorylinks = []
r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
categorylist = soup.find_all('div', {'data-content-type': 'button-item', 'data-appearance': 'default', 'data-element': 'main'})
for itemcategorylist in categorylist:
    for linkcategory in itemcategorylist.find_all('a', class_='pagebuilder-button-link', href=True):
        categorylinks.append(linkcategory['href'])

data = []
processed_urls = set()

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
                productlinks = []
                for hrefitem in itemlinks.find_all('a', class_='category-image', href=True):
                    url = hrefitem['href']
                    if url not in processed_urls:
                        productlinks.append(url)
                        processed_urls.add(url)

                        # simpan url ke csv
                        StancedUk = {'url': url}
                        data.append(StancedUk)
                        print('Saving', StancedUk['url'])
                        fields = ['url']
                        filename = 'test1.csv'

                        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            writer.writeheader()
                            for item in data:
                                writer.writerow(item)

print('Data is successfully saved in the file', filename)
