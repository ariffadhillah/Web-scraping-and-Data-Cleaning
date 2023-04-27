import requests
from bs4 import BeautifulSoup
import json
import csv

data = []

# membuat permintaan ke URL
url = 'https://automotivesuperstore.com.au/k-n-filters-re-0870'
r = requests.get(url)

# membuat objek BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others']
filename = 'test.csv'

# tabel Compatibility 
try:
    am_comp = soup.find('div', {'class': 'compatibility-container'})
    tables = am_comp.find_all('table', class_='ausct')
    result = {}
    # list_of_vehicle_compatibility = []
    for table in tables:
        brand = ''
        model = ''
        modelYears = ''
        spec_name = ''
        spec_value = ''
        rows = table.find_all('tr')
        for row in rows:
            if 'class' in row.attrs and 'ausctmh' in row['class']:
                brand = row.find('td', {'class': 'acc-head'}).text.strip()
            elif 'class' in row.attrs and 'ausctmh-container' in row['class']:
                model = row.find('td', {'class': 'acc-head'}).text.strip()
                if brand not in result:
                    result[brand] = {}
                if model not in result[brand]:
                    result[brand][model] = {}
            elif 'class' in row.attrs and 'ausctlh' in row['class']:
                modelYears = row.find('td', {'class': 'acc-head'}).text.strip()
                if spec_name not in result[brand][model]:
                    result[brand][model][modelYears] = {}
            elif 'class' in row.attrs and 'ausctlh' in row['class']:
                spec_name = row.find('td', {'class': 'acc-head'}).text.strip()
                spec_value = ''
            elif 'class' in row.attrs and 'ausctlh-container' in row['class']:
                spec_container = row.find('td')
                spec_value_parts = [x.strip() for x in spec_container.stripped_strings]
                spec_value = ','.join(spec_value_parts)
                result[brand][model][modelYears][spec_name] = spec_value
    list_of_vehicle_compatibility = json.dumps(result)
except:
    am_comp =''
    list_of_vehicle_compatibility = ''

# Specifications / Others
try:
    spec_group = soup.find('div', {'class': 'spec-group'})
    rows = spec_group.find_all('tr')
    specs = {}
    for row in rows:
        key = row.find('th').text.strip().replace(':', '')
        value = row.find('td').text.strip()
        specs[key] = value
    others = json.dumps(specs)
except:
    others = ''

Automotivesuperstore = {
    'Category (Parent)': '',
    'Category URL (Parent)': '',
    'Category - Leaf (Child 1)': '',
    'Category URL - Leaf (Child 1)': '',
    'Product URL': '',
    'PartNumber': '',
    'Product Title': '', 
    'Product Subtitle': '',
    'Product Description': '',
    'Image URLs': '',
    'Price': '',
    'List of Vehicle Compatibility': list_of_vehicle_compatibility.replace('Positions:,', 'Positions":"').replace('"": ', '').replace('Bay,Quantity', 'Bay","Quantity').replace('Quantity Per Vehicle:,', 'Quantity Per Vehicle":"'),
    'Brand': 'Automotivesuperstore',
    'OE number / cross-reference': '',
    'Others': others,
}

data.append(Automotivesuperstore)
print('Saving', Automotivesuperstore['List of Vehicle Compatibility'],Automotivesuperstore['Others'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print('Data is successfully saved in the file', filename)

