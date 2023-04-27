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
fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others']
filename = 'automotivesuperstore.csv'
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
                    url_Category_URL_Leaf_Child1 = hrefitem['href']
                    if url_Category_URL_Leaf_Child1 not in processed_urls:
                        processed_urls.add(url_Category_URL_Leaf_Child1)
                        print(url_Category_URL_Leaf_Child1)
                        page_num = 1
                        while True:
                            page_url = url_Category_URL_Leaf_Child1 + f'?p={page_num}'
                            r = requests.get(page_url, headers=headers)
                            soup = BeautifulSoup(r.content, 'lxml')
                            linkCategoryProducts = soup.find_all('a', class_='product photo product-item-photo', href=True)
                            if not linkCategoryProducts:
                                break
                            for linkCategoryProduct in linkCategoryProducts:
                                if linkCategoryProduct['href'] not in processed_urls:
                                    r = requests.get(linkCategoryProduct['href'] , headers=headers)
                                    soup = BeautifulSoup(r.content, 'lxml')
                                    # print(linkCategoryProduct['href'])
                                    # membuat objek BeautifulSoup
                                    # r = requests.get(linkCategoryProduct, headers=headers)
                                    # soup = BeautifulSoup(r.content, 'lxml')

                                    


                                    part_number_element = soup.find('div', class_='product attribute partnumber')
                                    if part_number_element:
                                        try:
                                            PartNumber = part_number_element.text.replace('Part No.', '').strip()    
                                        except:
                                            PartNumber = ''
                                    else:
                                        print(' ')

                                    try:
                                        productTitle = soup.find('h1', class_='page-title').text.strip()    
                                    except:
                                        productTitle = ''

                                    try:
                                        productDescription = soup.find('div', class_='product attribute description').text.strip()    
                                    except:
                                        productDescription = ''

                                    # gallery-placeholder
                                    try:
                                        imgproductmedia = soup.find('div', {'class': 'product media'})
                                        image = imgproductmedia.find('img', {'class': 'gallery-placeholder__image'})
                                        image_url = image['src']
                                    except:
                                        image_url = ''
                                    try:
                                        price_wrapper = soup.find('span', {'data-price-type': 'finalPrice'})
                                        price = price_wrapper.find('span', {'class': 'price'}).text
                                    except:
                                        price = ''


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
                                    Category_Leaf_Child = []
                                    Category_Leaf_Child.append('Home  ' + linkcategory.split('/')[-1].replace('-', ' ').title() + ' ' +  lintpro + ' ' + url_Category_URL_Leaf_Child1.split('/')[-1].replace('-', ' ').title())
                                    Automotivesuperstore = {
                                        'Category (Parent)': 'Home ' + linkcategory.split('/')[-1].replace('-', ' ').title(),
                                        'Category URL (Parent)': linkcategory,
                                        'Category - Leaf (Child 1)': ' '.join(Category_Leaf_Child).replace('\n', ' ').replace("['", "").replace("']",""),
                                        'Category URL - Leaf (Child 1)': url_Category_URL_Leaf_Child1,
                                        'Product URL': linkCategoryProduct['href'],
                                        'PartNumber': PartNumber,
                                        'Product Title': productTitle, 
                                        'Product Subtitle': '',
                                        'Product Description': productDescription,
                                        'Image URLs': image_url,
                                        'Price': price,
                                        'List of Vehicle Compatibility': list_of_vehicle_compatibility.replace('Positions:,', 'Positions":"').replace('"": ', '').replace('Bay,Quantity', 'Bay","Quantity').replace('Quantity Per Vehicle:,', 'Quantity Per Vehicle":"'),
                                        'Brand': 'Automotivesuperstore',
                                        'OE number / cross-reference': '',
                                        'Others': others,
                                    }

                                    data.append(Automotivesuperstore)
                                    print('Saving', Automotivesuperstore['PartNumber'],Automotivesuperstore['Category - Leaf (Child 1)'], Automotivesuperstore['Price'], Automotivesuperstore['Product URL'])
                                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                                        writer.writeheader()
                                        for item in data:
                                            writer.writerow(item)

                            # print('Data is successfully saved in the file', filename)
                            page_num += 1
                            time.sleep(1) # time sleep
