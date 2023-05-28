import requests
from bs4 import BeautifulSoup
import csv
import json
import time

baseurl = 'https://www.hardrace.co.uk/anti-roll-bar-drop-link-adjustable-0050292.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

try:
    productTitle = soup.find('h1', class_='page-title').text.strip()
except:
    productTitle = ''

try:
    productSubtitle = soup.find('td', {'data-th':'Subtitle'}, class_='col data' ).text.strip()
except:
    productSubtitle = ''

try:
    productinfomain = soup.find('td', {'data-th':'Subtitle'}, class_='col data' ).text.strip()
    discription_txt = soup.find('div', class_='product attribute overview').text.strip()
    discription_ul = soup.find('div', class_='hardraceProductPromo').text.strip()
    discription = productinfomain + 'br_row' + discription_txt + 'br_row' + discription_ul  
except:
    discription = ''


try:
    partNumberdiv = soup.find('div', class_='product attribute sku')
    partNumber = partNumberdiv.find('div', {'itemprop':'sku'}, class_='value' ).text.strip()
except:
    partNumber = ''

try:
    price_wrapper = soup.find('span', {'class': 'price-wrapper price-including-tax'})
    price = price_wrapper.find('span', {'class': 'price'}).text
except:
    price = ''

try:
    imgproductmedia = soup.find('div', {'class': 'gallery-placeholder _block-content-loading'})
    image = imgproductmedia.find('img', {'class': 'gallery-placeholder__image'})
    image_url = image['src']
except:
    image_url = ''

try:
    others = soup.find('div', {'class': 'product attribute description'}).text.strip()
except:
    others = ''


hardrace = {
    'Category (Parent)': '',
    'Category URL (Parent)': '',
    'Category - Leaf (Child 1)': '',
    'Category URL - Leaf (Child 1)': '',
    'Product URL': '',
    'PartNumber': partNumber,
    'Product Title': productTitle, 
    'Product Subtitle': productSubtitle,
    'Product Description': discription.replace('br_row', '\n'),
    'Image URLs': image_url,
    'Price': price,
    'List of Vehicle Compatibility': '',
    'Brand': 'hardrace',
    'Others': others,
}
if partNumber:
    data.append(hardrace)
    print('Saving', hardrace['Category (Parent)'],hardrace['Category URL (Parent)'], hardrace['Category - Leaf (Child 1)'], hardrace['Category URL - Leaf (Child 1)'], hardrace['Product URL'], hardrace['PartNumber'], hardrace['Product Title'], hardrace['Product Subtitle'], hardrace['Product Description'], hardrace['Image URLs'], hardrace['Price'], hardrace['List of Vehicle Compatibility'], hardrace['Brand'], hardrace['Others'])


