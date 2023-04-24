
import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://aeroflowperformance.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

r = requests.get('https://aeroflowperformance.com/air-filtration/air-filters/pod-filters')
soup = BeautifulSoup(r.content, 'lxml')

breadcrumbs = soup.find('ul', class_='items').find_all('a')
try:
    categoryParent = breadcrumbs[0].text.strip() + '  ' + breadcrumbs[1].text.strip()
    
except:
    categoryParent = ''

try:
    categoryParent_url = breadcrumbs[1]['href']
except:
    categoryParent_url = ''

breadcrumbscategoryParent = soup.find('ul', class_='items').find_all('li')
categoryLeafChild1 = ''
for breadcrumb in breadcrumbscategoryParent:
    categoryLeafChild1 += breadcrumb.text.strip() + ' '    
    categoryLeafChild1 += ' '  



breadcrumbscategoryParenturl = soup.find('ul', class_='items').find_all('a')
categoryLeafChild1_url = ''
for breadcrumb in breadcrumbscategoryParenturl:
    # categoryLeafChild1 += breadcrumb.text.strip() + ' '
    categoryLeafChild1_url = breadcrumb.get("href")
    # categoryLeafChild1 += '  '


productlist = soup.find_all('li', class_='item product product-item')

productlinks = set()

for item in productlist:
    for link in item.find_all('a', href=True):
        url = link['href']
        if url not in productlinks:
            productlinks.add(url)

data = []

for link in productlinks:
    try:
        r = requests.get(link, headers=headers)
    except:
        continue
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        partNumber = soup.find('div', class_='value sku').text.strip()
    except:
        partNumber = ''
    
    try:
        h1_tag = soup.find('h1', {'class': 'short-des'})
        productTitle = h1_tag.strong.text
        productSubtitle = h1_tag.text.replace(productTitle, '').strip()
    except:
        h1_tag = ''
        productTitle = ''
        productSubtitle = ''
    
    try:
        productDescription = soup.find('div', class_='data item content').text.strip()
    except:
        productDescription = ''
    
    try:
        price = soup.find('span', class_='price').text.strip()
    except:
        price = ''
    
    try:
        imageurl = soup.find('img', {"class":"gallery-placeholder__image"})['src']
    except:
        imageurl = ''

    Aeroflow  = {
        'Category (Parent)' : categoryParent,
        'Category URL (Parent)' : categoryParent_url,
        'Category - Leaf (Child 1)': categoryLeafChild1,
        'Category URL - Leaf (Child 1)': categoryLeafChild1_url,
        'Product URL': link,
        'PartNumber' : partNumber,
        'Product Title' : productTitle, 
        'Product Subtitle': productSubtitle,
        'Product Description': productDescription,
        'Image URLs': imageurl,
        'Price': price,
        'List of Vehicle Compatibility': ' ',
        'Brand': ' ',
        'OE number / cross-reference' : ' '
    }

    data.append(Aeroflow)
    print(data)

fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference']

filename = 'Aeroflow.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print('data is successfully saved in the file CSV', filename)


