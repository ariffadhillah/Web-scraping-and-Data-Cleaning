import requests
from bs4 import BeautifulSoup
import csv
import json
import time

# https://webshop.nrf.eu/catalog/category/view/s/automotive/id/41/?v_brand=5087&v_range=124&v_generatie=2016&v_fuel=B&v_size=1.4+%7C+125+KW+%7C+170+HP

# https://webshop.nrf.eu/catalog/category/view/s/automotive/id/41/?v_brand=5087&v_range=500&v_generatie=2008&v_fuel=B&v_size=1.4+%7C+103+KW+%7C+140+HP

baseurl = 'https://webshop.nrf.eu/catalog/category/view/s/automotive/id/41/?v_brand=5087&v_range=124&v_generatie=2016&v_fuel=B&v_size=1.4+%7C+125+KW+%7C+170+HP'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

data = []

# fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'Others']
# filename = 'Webshop.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

processed_urls = set()

produclinks = []


products_list = soup.find_all('div', class_='product-wrapper')
print(products_list)