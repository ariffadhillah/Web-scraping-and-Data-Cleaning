import requests
from bs4 import BeautifulSoup
import csv
import json
import time

baseurl = 'https://www.hardrace.co.uk/vehicle-search-new.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}

data = []

fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'Others']
filename = 'Hardrace.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

processed_urls = set()

produclinks = []

aplicarionNameCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

for catrList in aplicarionNameCars:
    for link in catrList.find_all('a', href=True):
        url = link['href']
        if url not in processed_urls:
            produclinks.append(url)
            processed_urls.add(url)

for make_name_url in produclinks:
    r = requests.get(make_name_url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    listItemCars = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')
    make_name = soup.find('h1', class_='page-title').text.strip()
    print(make_name_url, make_name)

    productItemLinks = []
    for product_item in listItemCars:
        for link_product_item in product_item.find_all('a', href=True):
            urlproduct = link_product_item['href']
            if urlproduct not in processed_urls:
                productItemLinks.append(urlproduct)
                processed_urls.add(urlproduct)

    for modelUrlName in productItemLinks:
        page_num_model = 1
        while True:
            page_url_model = modelUrlName + f'?p={page_num_model}'
            r = requests.get(page_url_model, headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')
            model_name = soup.find('h1', class_='page-title').text.strip()

            print(model_name, modelUrlName)

            linktypeUrl = []
            listTypeModel = soup.find_all('div', class_='col-12 col-md-4 mb-4 px-2')

            for ListTypeUrl in listTypeModel:
                for typeUrl in ListTypeUrl.find_all('a', class_='mt-auto', href=True):
                    texttypeUrl = typeUrl.text.strip()
                    linktypeUrl.append((typeUrl['href'], texttypeUrl))
                    
                
            for typeUrl, texttypeUrl in linktypeUrl:
                page_num = 1
                while True:
                    page_url = typeUrl + f'?p={page_num}'

                            
                    

                    r = requests.get(page_url, headers=headers)
                    soup = BeautifulSoup(r.content, 'lxml')
                    
                    resultType = []
                    resultType.append({
                        "make": make_name,
                        "model": model_name,
                        "type": texttypeUrl
                    })

                    list_of_Vehicle_Compatibility = json.dumps(resultType)
                    # print(typeUrl, texttypeUrl)

                    product_items = soup.find_all('strong', class_='product-item-name')
                    if not product_items:
                        break
                    for product_item in product_items:
                        productItem = product_item.find('a', class_='product-item-link', href=True)
                        if productItem:
                            link = productItem['href']
                        
                            r = requests.get(link, headers=headers)
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
                                partNumber = partNumberdiv.find('div',  class_='value' ).text.strip()
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

                            # print(productTitle, list_of_Vehicle_Compatibility.replace('[{', '{').replace('}]', '}'))


                            hardrace = {
                                'Category (Parent)': 'Home  ' + '  Applications',
                                'Category URL (Parent)': baseurl,
                                'Category - Leaf (Child 1)': 'Home   ' + ' Applications ' + '   ' + make_name + '   ' + model_name + '   ' + texttypeUrl,
                                'Category URL - Leaf (Child 1)': typeUrl,
                                'Product URL': link,
                                'PartNumber': f"'{partNumber}",
                                'Product Title': productTitle, 
                                'Product Subtitle': productSubtitle,
                                'Product Description': discription.replace('br_row', '\n'),
                                'Image URLs': image_url,
                                'Price': price.replace('£', ''),
                                'List of Vehicle Compatibility': list_of_Vehicle_Compatibility.replace('[{', '{').replace('}]', '}'),
                                'Brand': 'Hardrace',
                                'Others': others,
                            }
                            # if partNumber:
                            data.append(hardrace)
                            print('Saving',hardrace['Category - Leaf (Child 1)'], hardrace['Category URL - Leaf (Child 1)'], hardrace['Product URL'], hardrace['PartNumber'], hardrace['Product Title'])
                            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.DictWriter(csvfile, fieldnames=fields)
                                writer.writeheader()
                                for item in data:
                                    writer.writerow(item)

                    page_num += 1
            
            resultModel = []
            resultModel.append({
                "make": make_name,
                "model": model_name,
                "type": ''
            })
            list_of_Vehicle_Compatibility = json.dumps(resultModel)

            time.sleep(.5)

            product_items_model = soup.find_all('strong', class_='product-item-name')
            if not product_items_model:
                break
            for product_item in product_items_model:
                productItem_model = product_item.find('a', class_='product-item-link', href=True)
                if productItem_model:
                    link_model = productItem_model['href']
                        
                    r = requests.get(link_model, headers=headers)
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
                        partNumber = partNumberdiv.find('div',  class_='value' ).text.strip()
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
                    
                    # print(productTitle, list_of_Vehicle_Compatibility.replace('[{', '{').replace('}]', '}'))


                    hardrace = {
                        'Category (Parent)': 'Home  ' + '  Applications',
                        'Category URL (Parent)': baseurl,
                        'Category - Leaf (Child 1)': 'Home  ' + ' Applications ' + '   ' + make_name + '   ' + model_name,
                        'Category URL - Leaf (Child 1)': modelUrlName,
                        'Product URL': link_model,
                        'PartNumber': f"'{partNumber}",
                        'Product Title': productTitle, 
                        'Product Subtitle': productSubtitle,
                        'Product Description': discription.replace('br_row', '\n'),
                        'Image URLs': image_url,
                        'Price': price.replace('£', ''),
                        'List of Vehicle Compatibility': list_of_Vehicle_Compatibility.replace('[{', '{').replace('}]', '}'),
                        'Brand': 'hardrace',
                        'Others': others,
                    }
                    
                    # if partNumber:
                    data.append(hardrace)
                    print('Saving',hardrace['Category - Leaf (Child 1)'], hardrace['Category URL - Leaf (Child 1)'], hardrace['Product URL'], hardrace['PartNumber'], hardrace['Product Title'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for item in data:
                            writer.writerow(item)
            page_num_model += 1
