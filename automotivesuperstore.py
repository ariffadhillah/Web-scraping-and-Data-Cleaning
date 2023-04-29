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


fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference', 'Others', 'Other_fitment']
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

                                    
                                    dataresultcompatibility = []
                                    dataresultOther_fitment = []

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

                                    #/ Compatibility  the pure vehicle info json
                                    try:
                                        am_comp = soup.find('div', {'class': 'compatibility-container'})

                                        tables = am_comp.find_all('table', class_='ausct')
                                    
                                        for table in tables:
                                            titlebrand = table.find('tr', class_='ausctmh')
                                            make = titlebrand.text.strip()

                                            listbrand = table.find_all('tr', class_='ausctsh')
                                            for tr in listbrand:
                                                model_list = tr.find_all('td', class_='acc-head')
                                                for model in model_list:
                                                    model_text = model.text
                                                    listothers = tr.find_next_sibling('tr')
                                                    others_list = listothers.find_all('td', class_='acc-head')
                                                    for others in others_list:
                                                        others_text = others.text.strip()
                                                        dataresultcompatibility.append({"make": make, "model": model_text, "others": others_text})
                                        list_of_vehicle_compatibility = json.dumps(dataresultcompatibility)
                                        # print(json.dumps(dataresult, indent=2))
                                    except:
                                        list_of_vehicle_compatibility = ' '

                                    #/ Compatibility Other_fitment json
                                    try:
                                        divOther_fitment = soup.find('div', {'class': 'compatibility-container'})

                                        tables_Other_fitment = divOther_fitment.find_all('table', class_='ausct')
                                    
                                        for table_Other_fitment in tables_Other_fitment:
                                            
                                            trOther_fitment = table_Other_fitment.find_all('tr', class_='ausctlh-container')
                                            
                                            for trOther in trOther_fitment:
                                                fitment_data = {}
                                                Otherfitment = trOther.find_all('td')
                                                
                                                for fitment in Otherfitment:
                                                
                                                    Otherfitment_text = fitment.get_text(strip=True)
                                                    if ':' in Otherfitment_text:
                                                        key, value = Otherfitment_text.split(':', 1)
                                                        fitment_data[key] = value
                                                    else:
                                                        fitment_data['Positions'] = Otherfitment_text
                                                    
                                                dataresultOther_fitment.append(fitment_data)
                                        
                                        Other_fitment = json.dumps(dataresultOther_fitment)
                                                
                                    except:
                                        Other_fitment = ''

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
                                    
                                    # brand
                                    try:
                                        product_info_main = soup.find('div', {'class': 'product-info-main'})
                                        altimage = product_info_main.find('img')
                                        brand = altimage.get('alt')
                                        
                                    except:
                                        brand = ''

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
                                        'List of Vehicle Compatibility': list_of_vehicle_compatibility,
                                        'Brand': brand,
                                        'OE number / cross-reference': '',
                                        'Others': others,
                                        'Other_fitment': Other_fitment.replace('To ~','","To":"').replace('Quantity Per Vehicle:','","Quantity Per Vehicle":"').replace('Product Fitment Note:','","Product Fitment Note":"').replace('": "','":"').replace('Catalog Type:Roll Control','","Catalog Type:Roll Control').replace('Fitment Retail:','","Fitment Retail":"').replace('PAFootNote1:','","PAFootNote1":"').replace('Catalog Type:', 'Catalog Type":"').replace('Catalog Type','","Catalog Type').replace('"",','').replace('PAFootNote2:','","PAFootNote2":"').replace('PAFootNote3:','","PAFootNote3":"').replace('Outcome:','","Outcome":"'),
                                    }

                                    data.append(Automotivesuperstore)
                                    print('Saving', Automotivesuperstore['Brand'], Automotivesuperstore['PartNumber'],Automotivesuperstore['Category - Leaf (Child 1)'], Automotivesuperstore['Price'], Automotivesuperstore['Product URL'], Automotivesuperstore['Others'])
                                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                                        writer.writeheader()
                                        for item in data:
                                            writer.writerow(item)

                            # print('Data is successfully saved in the file', filename)
                            page_num += 1
                            time.sleep(1) # time sleep
