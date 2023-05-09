import requests
from bs4 import BeautifulSoup
import csv
import time

# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }
# processed_urls = set()

# # Page Brake pads
# # brake_caliper = baseurl + '/products/brake_caliper/index.html'


# # r = requests.get(brake_caliper, headers=headers)
# # soup = BeautifulSoup(r.content, 'lxml')

# # listCarsName = []
# # listImportedCar = []
# # data = []
# # list_Brake_caliper = []

# # links_index2 = []
# # linkModel = []
# # leftmenuindex1 = soup.find('div', id='leftmenu_index2')
# # for urlCarsList in leftmenuindex1.find_all('a', href=True):
# #     links_index2.append(urlCarsList['href'])

# # for crasListBrakeCaliper in links_index2:
# #     r = requests.get(crasListBrakeCaliper, headers=headers)
# #     soup = BeautifulSoup(r.content, 'lxml')
    
# #     listCarsBrakeCaliper = soup.find_all('div', id='maker_icons')
    
# #     for listMake in listCarsBrakeCaliper:
# #         for linkMake in listMake.find_all('a', href=True):
# #             linkModel.append(linkMake['href'])

# # for linkMake in linkModel:
# #     r = requests.get(linkMake, headers=headers)
# #     soup = BeautifulSoup(r.content, 'lxml')

# #     test = soup.find('div', class_='maintitle_pc_box2')
# #     print(test.text.strip())



# # testModel = 'https://www.endless-sport.co.jp/products/brake_caliper/car_list/list_lexus_2022.html'

# # r = requests.get(testModel, headers=headers)
# # soup = BeautifulSoup(r.content, 'lxml')

# # data = []
# # iframesimport = soup.find_all('iframe')
# # for iframeimport in iframesimport:
# #     src = iframeimport['src']
# #     iframeimport_content = requests.get(src).content
# #     iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
# #     tables = iframeimport_soup.find_all('table')
        
# #     for tablemodelimport in tables:
# #         rowsmodelimport = tablemodelimport.find_all('tr')[2]
# #         modelimport =  rowsmodelimport.find_all('td')[1]
        
# #     for table in tables:
# #         rows = table.find_all('tr')[5:]
# #         for row in rows:
# #             # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
# #             if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
# #                 continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
# #             year = row.find_all('td')
# #             engine = row.find_all('td')
# #             type_ = row.find_all('td')
# #             PartNumberFront = row.find_all('td')
# #             PartNumberRear = row.find_all('td')[10:]
# #             if PartNumberFront and PartNumberRear:
# #                 PartNumber = PartNumberFront[5].text.strip() +' '+ PartNumberRear[0].text.strip()
# #             else:
# #                 PartNumber = ""
    
# #             if year and engine and type_ and PartNumber:
# #                 endless = {
# #                     'Parttype (category)': '',
# #                     'Parttype URL (category)': '',
# #                     'Make': '',
# #                     'Make URL': '',
# #                     'Model': modelimport.text.strip(),
# #                     'Model URL': '',
# #                     'Year': year[1].text.strip(),
# #                     'Engine cc': ' ',
# #                     'Type': '',
# #                     'PartNumber': '',
# #                 }
# #                 data.append(endless)
# #                 print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])




           
#     # for table in tables:
#     #     rows = table.find_all('tr')[5:]
#     #     for row in rows:
#     #         # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
#     #         if row.has_attr('style') and row['style'].startswith('height: 149px'):
#     #             continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
#     #         cells = row.find_all('td')
#     #         year = cells[1].text.strip()
#     #         # PartNumberFront = cells[5].text.strip()
#     #         # PartNumberRear = cells[3].text.strip()
#     #         # PartNumber = f'{PartNumberFront} {PartNumberRear}' if PartNumberFront and PartNumberRear else ''
#     #         endless = {
#     #             'Parttype (category)': '',
#     #             'Parttype URL (category)': '',
#     #             'Make': '',
#     #             'Make URL': '',
#     #             'Model': modelimport,
#     #             'Model URL': '',
#     #             'Year': year,
#     #             'Engine cc': '',
#     #             'Type': '',
#     #             'PartNumber': '',
#     #         }
#     #         data.append(endless)
#     #         print('Saving', endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])

#     # for table in tables:
#     #     rows = table.find_all('tr')[5:]
#     #     for row in rows:
#     #         # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
#     #         if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#     #             continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
#     #         try:    
#     #             td_elements = row.find_all('td')
#     #             PartNumber = td_elements[6].text.strip()
#     #             # tambahkan kondisi untuk memeriksa panjang PartNumber
#     #             if len(PartNumber) < 10:
#     #                 continue            

#     #             type_ = row.find_all('td')
#     #             print(type_)
                
#     #             if PartNumber and type_:
#     #                 endless = {
#     #                     'Parttype (category)': '',
#     #                     'Parttype URL (category)': '',
#     #                     'Make': '',
#     #                     'Make URL': '',
#     #                     'Model': '',
#     #                     'Model URL': '',
#     #                     'Year': '',
#     #                     'Engine cc': '',
#     #                     'Type': type_,
#     #                     'PartNumber': PartNumber,
#     #                 }
#     #                 data.append(endless)
#     #                 print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
            
#     #         except:
#     #             None


testModel = 'https://www.endless-sport.co.jp/products/brake_caliper/car_list/list_toyota_2022.html'

r = requests.get(testModel)
soup = BeautifulSoup(r.content, 'lxml')

data = []
make = soup.find('div', class_="maintitle_pc_box2").text.strip()


iframesimport = soup.find_all('iframe')
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
                if len(type_) < 1:
                    continue
                PartNumber = td_elements[6].text.strip()
                if len(PartNumber) < 10:
                    continue
                if  type_ and PartNumber and make:
                    endless = {
                        'Parttype (category)': '',
                        'Parttype URL (category)': '',
                        'Make': make,
                        'Make URL': '',
                        'Model': '',
                        'Model URL': '',
                        'Year': '',
                        'Engine cc': '',
                        'Type': type_,
                        'PartNumber': PartNumber,
                    }
                    data.append(endless)
                    print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])
            except:
                None






# for iframeimport in iframesimport:
#     src = iframeimport['src']
#     iframeimport_content = requests.get(src).content
#     iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#     tables = iframeimport_soup.find_all('table')

#     for table in tables:
#         rows = table.find_all('tr')[5:]
#         for row in rows:
#             # tambahkan kondisi untuk memeriksa apakah elemen tr memiliki atribut style yang mengatur tinggi
#             if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#                 continue  # lewati jika ada atribut style dengan ketinggian yang ditentukan
                
#             td_elements = row.find_all('td')
#             try:
#                 partNumber = td_elements[6]
#                 print(partNumber.text)
#             except:
#                 continue
            
    


# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.endless-sport.co.jp/products/brake_caliper/car_list/list_toyota_2022.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'lxml')

# data = []

# iframesimport = soup.find_all('iframe')

# for iframeimport in iframesimport:
#     src = iframeimport['src']
#     iframeimport_content = requests.get(src).content
#     iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#     tables = iframeimport_soup.find_all('table')

#     for table in tables:
#         rows = table.find_all('tr')[5:]
#         for i, row in enumerate(rows):
#             if '税込価格' in row.text:
#                 continue
#             if i == 0:
#                 continue # Skip the first row (header row)
#             tds = row.find_all('td')
#             if len(tds) == 9:
#                 part_number = tds[5].text.strip()
#                 if tds[5].has_attr('rowspan'):
#                     rowspan = int(tds[5]['rowspan'])
#                     for j in range(rowspan+1):
#                         next_row = rows[i+j+2]
#                         next_tds = next_row.find_all('td')
#                         part_number += ' ' + next_tds[5].text.strip()
#                 print(part_number)




















# url = 'https://www.endless-sport.co.jp/products/brake_caliper/car_list/list_lexus_2022.html'


# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.endless-sport.co.jp/products/brake_caliper/car_list/list_toyota_2022.html'
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# data = []

# iframesimport = soup.find_all('iframe')
# for iframeimport in iframesimport:
#     src = iframeimport['src']
#     iframeimport_content = requests.get(src).content
#     iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#     tables = iframeimport_soup.find_all('table')

#     for tablebrake_caliper in tables:
#         rowtablebrake_caliper = tablebrake_caliper.find_all('tr')[2]
#         modelTablebrake_caliper =  rowtablebrake_caliper.find_all('td')[1].text.strip()
  
#     # for tablebrake_caliper in tables:
#     #     rowtablebrake_caliper = tablebrake_caliper.find_all('tr')[2]
#     #     modelTablebrake_caliper =  rowtablebrake_caliper.find_all('td')[1].text.strip()

#     for table in tables:
#         current_part_number = ''
#         current_type = ''
#         current_type_product_name = ''

#         # rows = table.find_all('tr')[5:]
#         # for no, row in enumerate(rows):
#         #     if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#         #         continue

#     for table in tables:
#         rows = table.find_all('tr')[5:]
#         for i, row in enumerate(rows):
#             if '税込価格' in row.text:
#                 continue
#             if i == 0:
#                 continue # Skip the first row (header row)
#             tds = row.find_all('td')
#             if len(tds) == 10:
#                 part_number = tds[6].text.strip()
#                 if tds[4].has_attr('rowspan'):
#                     rowspan = int(tds[6]['rowspan'])
#                     # print(rowspan)
#                     for j in range(rowspan+1):
#                         next_row = rows[i+j+1]
#                         next_tds = next_row.find_all('td')
#                         part_number += ' ' + next_tds[6].text.strip()
#             # if len(tds) == 10:
#                 type_item = tds[1].text.strip()
#                 if tds[0].has_attr('rowspan'):
#                     rowspan = int(tds[1]['rowspan'])
#                     # print(rowspan)
#                     for j in range(rowspan+1):
#                         next_row = rows[i+j+1]
#                         next_tds = next_row.find_all('td')
#                         type_item += ' ' + next_tds[1].text.strip()
#                 # print(part_number)
#             if len(tds) == 10:
#                 type_product = tds[2].text.strip()                

#                 endless = {
#                     'Parttype (category)': '',
#                     'Parttype URL (category)': '',
#                     'Make': '',
#                     'Make URL': '',
#                     'Model': modelTablebrake_caliper,
#                     'Model URL': '',
#                     'Year': '',
#                     'Engine cc': '',
#                     'Type': type_item + ' ' + type_product ,
#                     'PartNumber': part_number,
#                     }
#                 data.append(endless)
#                 print('Saving' , endless['Make'] , endless['Model']  ,   endless['Type'] ,  endless['PartNumber'])
            
#             # if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
#             #     continue
#             # if 'アイテム' in row.text:
#             #     continue

# # for no, tr in enumerate(allRows):
# #     tmp = []
# #     for td_no, data in enumerate(tr.find_all('td')):
# #         print  data.has_key("rowspan")
# #         if data.has_key("rowspan"):
# #             rowspan.append((no, td_no, int(data["rowspan"]), data.get_text()))


         


           

                       

            
#             # try:
#             #     type_ = td_elements[1]
#             #     if type_.has_attr('rowspan') and type_['rowspan'] == '2':
#             #         current_type = type_.text.strip()
#             #     type__value = current_type or type_.text.strip()
#             # except:
#             #     continue            

#             # try:
#             #     part_number = td_elements[6]  # change to index 5 (6th column)
#             #     if part_number.has_attr('rowspan') and part_number['rowspan'] == '2':
#             #         current_part_number = part_number.text.strip()
#             #     part_number_value = current_part_number or part_number.text.strip()
#             # except:
#             #     continue
           

#             # if type__value and part_number_value :
#             #     endless = {
#             #     'Parttype (category)': '',
#             #     'Parttype URL (category)': '',
#             #     'Make': '',
#             #     'Make URL': '',
#             #     'Model': modelTablebrake_caliper,
#             #     'Model URL': '',
#             #     'Year': '',
#             #     'Engine cc': '',
#             #     'Type': type__value,
#             #     'PartNumber': part_number_value,
#             #     }
#             #     data.append(endless)
#             #     print('Saving' , endless['Make'] , endless['Model']  ,   endless['Type'] ,  endless['PartNumber'])