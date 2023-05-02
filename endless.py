import requests
from bs4 import BeautifulSoup
import csv
import json
import time

baseurl = 'https://www.endless-sport.co.jp/products/products_index.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}


processed_urls = set() 

categoryProduct = []
r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
productList = soup.find_all('div', {'class': 'contents_box_triple'})

productLinks = []

for itemCategory in productList:
    for linkItemCategory in itemCategory.find_all('a', text='製品インデックス'):
        print(linkItemCategory['href'])
