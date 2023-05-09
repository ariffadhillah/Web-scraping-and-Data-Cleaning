# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# # import time

# # baseurl = 'https://www.endless-sport.co.jp'
# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# # }

# # processed_urls = set()
# # categoryProduct = []
# # listImportedCar = []

# # pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

# # r = requests.get(pageBrakepads, headers=headers)
# # soup = BeautifulSoup(r.content, 'lxml')
# # listCarsName = []
# # data = []

# # brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
# # importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
# # for linkcarsimported in importedCar.find_all('a', href=True):
# #     urlimported = linkcarsimported['href'].replace('https://', 'https://www.')
# #     if urlimported not in processed_urls:
# #         listImportedCar.append(urlimported)
# #         processed_urls.add(urlimported)

# # for pageCarListImport in listImportedCar:
# #     r = requests.get(pageCarListImport, headers=headers)
# #     soup = BeautifulSoup(r.content, 'lxml')    

# #     # testdiv = soup.find('div', id='maintitle_pc')
# #     # print(testdiv)

# #     cautionContents = soup.find('div', {'class': 'caution_contents'}) or soup.find('div', {'id': 'caution_contents'})
# #     if cautionContents:
# #         caution_links = cautionContents.find_all('a')
# #         category = caution_links[1]
# #         parttype_category_url = category['href']
# #         parttype_category = category.text.strip()


# #     iframesimport = soup.find_all('iframe')
# #     for iframeimport in iframesimport:
# #         src = iframeimport['src']
# #         iframeimport_content = requests.get(src).content
# #         iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
# #         tablesimport = iframeimport_soup.find_all('table')
# #         # print(tables)
# #         for tableMake in tablesimport:
# #             rowsMake = tableMake.find_all('tr')[1]
# #             makeimport =  rowsMake.find_all('td')[1]
        
# #         for tablemodelimport in tablesimport:
# #             rowsmodelimport = tablemodelimport.find_all('tr')[2]
# #             modelimport =  rowsmodelimport.find_all('td')[1]
            

# #         for table in tablesimport:
# #             rows = table.find_all('tr')[5:]
# #             for row in rows:
# #                 # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
# #                 if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
# #                     continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
# #                 year = row.find_all('td')
# #                 engine = row.find_all('td')
# #                 type_ = row.find_all('td')
# #                 PartNumberFront = row.find_all('td')
# #                 PartNumberRear = row.find_all('td')[10:]
# #                 if PartNumberFront and PartNumberRear:
# #                     PartNumber = PartNumberFront[5].text.strip() +' '+ PartNumberRear[0].text.strip()
# #                 else:
# #                     PartNumber = ""
                
# #                 if year and engine and type_ and PartNumber:
# #                     endless = {
# #                         'Parttype (category)': parttype_category,
# #                         'Parttype URL (category)': parttype_category_url,
# #                         'Make': makeimport.text.strip(),
# #                         'Make URL': '',
# #                         'Model': modelimport.text.strip(),
# #                         'Model URL': '',
# #                         'Year': year[3].text.strip().replace('～', ' ～ '),
# #                         'Engine cc': ' ',
# #                         'Type': type_[4].text.strip(),
# #                         'PartNumber': PartNumber.replace(' ', '\n'),
# #                     }
# #                     data.append(endless)
# #                     print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
                    
# #                     # with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
# #                     #     writer = csv.DictWriter(csvfile, fieldnames=fields)
# #                     #     writer.writeheader()
# #                     #     for item in data:
# #                     #         writer.writerow(item)




# from bs4 import BeautifulSoup

# html = '''
# <div class="slidebox2"><h1>title 1</h1>subtitle 1</div>
# <table>
#     <tr>
#         <td>part number 17909</td>
#     </tr>
#     <tr>
#         <td>data hasil 40 </td>
#     </tr>
# </table>
# <div class="slidebox2"><h1>title 2</h1>subtitle 2</div>
# <table>
#     <tr>
#         <td>part number 17</td>        
#     </tr>
#     <tr>
#         <td>data hasil 15 </td>
#     </tr>
# </table>
# <div class="slidebox2"><h1>title 3</h1>subtitle 3</div>
# <table>
#     <tr>
#         <td>part number 56</td>        
#     </tr>
#     <tr>
#         <td>data hasil 40 </td>
#     </tr>
# </table>
# '''

# soup = BeautifulSoup(html, 'html.parser')

# data = []

# # loop through all tables
# for table in soup.find_all('table'):
#     # get the title and subtitle
#     title = table.find_previous_sibling('div', class_='slidebox2').h1.text.strip()
#     subtitle = table.find_previous_sibling('div', class_='slidebox2').text.strip()

#     # get the data from the table
#     part_number = table.find('tr').td.text.strip()
#     data_hasil = table.find_all('tr')[1].td.text.strip()

#     # create the dictionary
#     endless = {
#         'Parttype (category)': '',
#         'Parttype URL (category)': '',
#         'Make': title,
#         'Make URL': '',
#         'Model': '',
#         'Model URL': '',
#         'Year': '',
#         'Engine cc': '',
#         'Type': subtitle,
#         'PartNumber': part_number,
#         'Data Hasil': data_hasil
#     }

#     # append the dictionary to the list
#     data.append(endless)

#     # print the result
#     print(f'{title}\t{subtitle}\t{part_number}\t{data_hasil}')

# # print(data)



import requests
from bs4 import BeautifulSoup

testModel = 'https://www.endless-sport.co.jp/products/brake_caliper/car_list/list_toyota_2022.html'

r = requests.get(testModel)
soup = BeautifulSoup(r.content, 'lxml')

data = []
make = soup.find('div', class_="maintitle_pc_box2").text.strip()

divmodel = soup.find_all('div', class_='slidebox2')

for div in divmodel:
    model = div.h1.text.strip()
    # print(model)
    enginecc = div.text.replace(model, '').strip()

    iframesimport = div.find_next_sibling('div').find_all('iframe')
    for iframeimport in iframesimport:
        src = iframeimport['src']
        iframeimport_content = requests.get(src).content
        iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
        tables = iframeimport_soup.find_all('table')

        for table in tables:
            PartNumber = []
            rows = table.find_all('tr')
            for row in rows:
                if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                    continue
                td_elements = row.find_all('td')
                try:
                    type_ = td_elements[1].text.strip()
                    if len(type_) < 0:
                        continue
                    PartNumber = td_elements[6].text.strip()
                    if len(PartNumber) < 10:
                        continue
                    if  type_ and PartNumber:
                        endless = {
                            'Parttype (category)': '',
                            'Parttype URL (category)': '',
                            'Make': make,
                            'Make URL': '',
                            'Model': model,
                            'Model URL': '',
                            'Year': '',
                            'Engine cc': enginecc,
                            'Type': type_,
                            'PartNumber': PartNumber,
                        }
                        data.append(endless)
                        print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
                except:
                    None
