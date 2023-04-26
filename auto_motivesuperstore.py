import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.stanceplus.com'


    r = requests.get(linkcategory, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = []
    productItem = soup.find_all('div', class_='panel-collapse collapse')
    for item in productItem:
        for href in item.find_all('a', class_='', href=True ):
            productList.append(baseurl + href['href'])

    for link in productList:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        productTitle = soup.find('h1', class_='item-title').text.strip()

        try:
            productSubtitle = soup.find('h2', class_='item-title').text.strip()
        except:
            productSubtitle = ''
        try:
            productDescription = soup.find('div', {'class': 'col_three_fifth item-desc col_last'}).find('p').text.strip()
        except:
            productDescription = ''

        try:
            price = soup.find('div', class_='item-price').text.strip()
        except:
            price = ''
        
        sectionimage_url = soup.find('section', {'class': 'hero'})        
        try:
            image_url = baseurl + sectionimage_url.find('a', {'class': 'image'}).get('href')
        except:
            image_url = ''    

        table_List_of_Vehicle_Compatibility = soup.find('section', {'class': 'hero'}).find('div', {'class': 'table table-striped table-bordered'})
        if table_List_of_Vehicle_Compatibility:
            table_rows_List_of_Vehicle_Compatibility = table_List_of_Vehicle_Compatibility.find_all('tr')
            List_of_Vehicle_Compatibility = []
            for row in table_rows_List_of_Vehicle_Compatibility:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                List_of_Vehicle_Compatibility.append(cols)
        else:
            List_of_Vehicle_Compatibility = ''

        StancedUk = {
            'Category (Parent)': linkcategory.split('/')[-1].replace('-', ' ').title(),
            'Category URL (Parent)': linkcategory,
            'Category - Leaf (Child 1)': '',
            'Category URL - Leaf (Child 1)': '',
            'Product URL': link,
            'PartNumber': link.split("/")[-2] + "/" + link.split("/")[-1] + "/",
            'Product Title': productTitle, 
            'Product Subtitle': productSubtitle,
            'Product Description': productDescription,
            'Image URLs': image_url,
            'Price': price,
            'List of Vehicle Compatibility': List_of_Vehicle_Compatibility,
            'Brand': 'STANCED UK',
            'OE number / cross-reference': ''
        }

        data.append(StancedUk)
        print(StancedUk)

        fields = ['Category (Parent)', 'Category URL (Parent)', 'Category - Leaf (Child 1)', 'Category URL - Leaf (Child 1)', 'Product URL', 'PartNumber', 'Product Title', 'Product Subtitle', 'Product Description', 'Image URLs', 'Price', 'List of Vehicle Compatibility', 'Brand', 'OE number / cross-reference']

        filename = 'Test Stanced Uk.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item)

        print('data is successfully saved in the file CSV', filename)