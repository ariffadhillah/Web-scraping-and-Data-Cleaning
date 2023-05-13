import requests
from bs4 import BeautifulSoup
import csv
import time

data = []


# # # ///////////////////////////////////////////////////////////


baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

# brake_line = baseurl + '/products/brake_line/index.html'

# r = requests.get(brake_line, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# listbrake_line = soup.find('select', onchange='location.href=value;')

# itembrake_line = listbrake_line.find_all('option')[:10]
# linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]
# # listbrake_linelinks.append(linknameCarsbrake_line)
# # print(linknameCarsbrake_line)

# for listbrake_linelinks in linknameCarsbrake_line:
#     r = requests.get(listbrake_linelinks, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')
    
#     makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
#     divmodel = soup.find_all('div', class_='slidebox2')

#     for div in divmodel:
#         modelbraek_line = div.text.strip() 
                
#         iframesimport = div.find_next_sibling('div').find_all('iframe')
#         for iframeimport in iframesimport:
#             src = iframeimport['src']
#             iframeimport_content = requests.get(src).content
#             iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#             tables = iframeimport_soup.find_all('table')
            
#             year = ''       
#             model =''
#             typebraek_line = ''
#             partNumberbraek_line = ''
#             series = ''
            
#             for table in tables:
#                 rows = table.find_all('tr')[3:]
#                 for row in rows:
#                     try:
#                         td_elementspartNumber = row.find_all('td')
#                         # Seri
#                         if len(td_elementspartNumber) == 15:
#                             partNumberbraek_line = td_elementspartNumber[3].text.strip()
#                         elif len(td_elementspartNumber) == 14:
#                             partNumberbraek_line = td_elementspartNumber[2].text.strip()
#                         else:
#                             partNumberbraek_line = ' '
#                     except:
#                         partNumberbraek_line = ''

#                     try:                    
#                         td_elementstypebraek_line = row.find_all('td')
#                         if len(td_elementstypebraek_line) == 15:
#                             typebraek_line = td_elementstypebraek_line[2].text.strip()
#                         elif len(td_elementstypebraek_line) == 14:
#                             typebraek_line = td_elementstypebraek_line[1].text.strip()
#                         else:
#                             typebraek_line = ''
#                     except:
#                         typebraek_line = ' '
                    
#                     # print(modelbraek_line, typebraek_line, partNumberbraek_line)

#                     if typebraek_line and partNumberbraek_line:
#                         endless = {
#                             'Parttype (category)': 'ブレーキライン',
#                             'Parttype URL (category)': '',
#                             'Make': makebraek_line,
#                             'Make URL': listbrake_linelinks,
#                             'Model':  modelbraek_line,
#                             'Model URL': '',
#                             'Year':  '',
#                             'Series': '',
#                             'Engine cc': '',
#                             'Type': typebraek_line,
#                             'PartNumber':partNumberbraek_line,
#                         }
#                         data.append(endless)
#                         print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])

        



# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# brake_line = baseurl + '/products/brake_line/index.html'

# r = requests.get(brake_line, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# listbrake_line = soup.find('select', onchange='location.href=value;')

# itembrake_line = listbrake_line.find_all('option')[10:]
# linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]
# # listbrake_linelinks.append(linknameCarsbrake_line)
# # print(linknameCarsbrake_line)

# for listbrake_linelinks in linknameCarsbrake_line:
#     r = requests.get(listbrake_linelinks, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')
    
#     makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
#     divmodel = soup.find_all('div', class_='slidebox2')

#     for div in divmodel:
#         modelbraek_line = div.text.strip() 
                
#         iframesimport = div.find_next_sibling('div').find_all('iframe')
#         for iframeimport in iframesimport:
#             src = iframeimport['src']
#             iframeimport_content = requests.get(src).content
#             iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#             tables = iframeimport_soup.find_all('table')
            
#             year = ''       
#             model =''
#             typebraek_line = ''
#             partNumberbraek_line = ''
#             series = ''
                    
#             for table in tables:
#                 rows = table.find_all('tr')[4:]
#                 for row in rows:
#                     td_elementsmodel = row.find_all('td')
#                     try:
#                         if len(td_elementsmodel) == 11:
#                             model = td_elementsmodel[1].text.strip()                    
#                     except:
#                         None                
                
#                     try:
#                         td_elementsyear = row.find_all('td')
#                         if len(td_elementsyear) == 11:
#                             year = td_elementsyear[3].text.strip()
#                         elif len(td_elementsyear) == 10:
#                             year = td_elementsyear[2].text.strip()
#                         else:
#                             year = ' '
#                     except:
#                         year = ' '
                    
#                     try:
#                         # Seri
#                         td_elementsseries = row.find_all('td')
#                         if len(td_elementsseries) == 11:
#                             series = td_elementsseries[4].text.strip()
#                         elif len(td_elementsseries) == 10:
#                             series = td_elementsseries[3].text.strip()
#                         else:
#                             series = '  '
#                     except:
#                         series = '  '
                        
#                     try:
#                         td_elementspartNumber = row.find_all('td')
#                         # Seri
#                         if len(td_elementspartNumber) == 11:
#                             partNumberbraek_line = td_elementspartNumber[5].text.strip()
#                         elif len(td_elementspartNumber) == 10:
#                             partNumberbraek_line = td_elementspartNumber[4].text.strip()
#                         else:
#                             partNumberbraek_line = ' '
#                     except:
#                         partNumberbraek_line = ''

#                     try:                    
#                         td_elementstypebraek_line = row.find_all('td')
#                         if len(td_elementstypebraek_line) == 11:
#                             typebraek_line = td_elementstypebraek_line[2].text.strip()
#                         elif len(td_elementstypebraek_line) == 10:
#                             typebraek_line = td_elementstypebraek_line[1].text.strip()
#                         else:
#                             typebraek_line = ''
#                     except:
#                         typebraek_line = ' '

#                     endless = {
#                         'Parttype (category)': 'ブレーキライン',
#                         'Parttype URL (category)': brake_line,
#                         'Make': modelbraek_line,
#                         'Make URL': listbrake_linelinks,
#                         'Model':  model,
#                         'Model URL': '',
#                         'Year':  year,
#                         'Series': 'Series   ' + series,
#                         'Engine cc': '',
#                         'Type': typebraek_line,
#                         'PartNumber':partNumberbraek_line,
#                     }
#                     data.append(endless)
#                     print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])




# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# # Page Brake pads

# brake_rotor = baseurl + '/products/brake_rotor/index.html'

# r = requests.get(brake_rotor, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# # tekigou_icon

# listbrakerotor = soup.find_all('div', class_='tekigou_icon')[1:]

# listbrakerotorlinks = []

# for itembrakerotor in listbrakerotor:
#     for namecarslistbrakerotor in itembrakerotor.find_all('a', href=True):
#         # print(namecarslistbrakerotor['href']) 
#          listbrakerotorlinks.append(namecarslistbrakerotor['href']) 

# for pagelistbrakerotor in listbrakerotorlinks:
#     r = requests.get(pagelistbrakerotor, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     try:
#         makebrakerotor = soup.find('div', 'maintitle_pc_box2').text.strip()
#     except:
#         makebrakerotor = ''
        
#     divmodel = soup.find_all('div', class_='slidebox2')[1:]
        
#     for div in divmodel:
#         modelbrakerotor = div.text.strip() 
            
#         iframesimport = div.find_next_sibling('div').find_all('iframe')
#         for iframeimport in iframesimport:
#             src = iframeimport['src']
#             iframeimport_content = requests.get(src).content
#             iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#             tables = iframeimport_soup.find_all('table')

#             year = ''       
#             model =''
#             typebraek_line = ''
#             partNumberbraek_line = ''
#             series = ''
                    
#             for table in tables:
#                 rows = table.find_all('tr')[4:]
#                 for row in rows:
#                     td_elementsmodel = row.find_all('td')
#                     removetext = ['test']
#                     if any(text in td.text.strip() for td in td_elementsmodel for text in removetext):
#                         continue
#                     try:
#                         if len(td_elementsmodel) == 8:
#                             model = td_elementsmodel[1].text.strip()   
#                         elif len(td_elementsmodel) == 7:
#                             continue
#                         else:
#                             model = td_elementsmodel[1].text.strip()   
                                             
#                     except:
#                         None                
                   
#                     td_elementspartNumber = row.find_all('td')
#                     removetext = ['test']
#                     if any(text in td.text.strip() for td in td_elementspartNumber for text in removetext):
#                         continue
#                     try:
#                         if len(td_elementspartNumber) == 8:
#                             partNumberbrakerotor = td_elementspartNumber[2].text.strip()   
#                         elif len(td_elementspartNumber) == 7:
#                             continue
#                         else:
#                             partNumberbrakerotor = td_elementspartNumber[2].text.strip()   
                                             
#                     except:
#                         None      
                   
#                     endless = {
#                         'Parttype (category)': 'ブレーキライン',
#                         'Parttype URL (category)': '',
#                         'Make': makebrakerotor,
#                         'Make URL': '',
#                         'Model':  modelbrakerotor,
#                         'Model URL': '',
#                         'Year':  '',
#                         'Series': model,
#                         'Engine cc': '',
#                         'Type': '',
#                         'PartNumber':partNumberbrakerotor,
#                     }
#                     data.append(endless)
#                     print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])





# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# # Page Brake pads

# brake_rotor = baseurl + '/products/brake_rotor/index.html'

# r = requests.get(brake_rotor, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# # tekigou_icon

# listbrakerotor = soup.find_all('div', class_='tekigou_icon')[1:]

# listbrakerotorlinks = []

# for itembrakerotor in listbrakerotor:
#     for namecarslistbrakerotor in itembrakerotor.find_all('a', href=True):
#         # print(namecarslistbrakerotor['href']) 
#          listbrakerotorlinks.append(namecarslistbrakerotor['href']) 

# for pagelistbrakerotor in listbrakerotorlinks:
#     r = requests.get(pagelistbrakerotor, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')


# benar suspension

# url ='https://www.endless-sport.co.jp/products/suspension/index_lexus.html'

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# makebrakerotor = soup.find('div', 'maintitle_pc_box2').text.strip()

# divmodel = soup.find_all('div', class_='slidebox2')[1:]        
# for div in divmodel:
#     engine_cc = div.text.strip() 
            
#     iframesimport = div.find_next_sibling('div').find_all('iframe')
#     for iframeimport in iframesimport:
#         src = iframeimport['src']
#         iframeimport_content = requests.get(src).content
#         iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#         tables = iframeimport_soup.find_all('table')

#         for table in tables:
#             rows = table.find_all('tr')[7:]
#             for row in rows:
#                 td_elements = row.find_all('td')
#                 # print(td_elements)
#                 removetext = ['test']
#                 if any(text in td.text.strip() for td in td_elements for text in removetext):
#                     continue
#                 try:
#                     if len(td_elements) == 15:
#                         CarsMake = td_elements[1].text.strip()
#                     else:
#                         CarsMake = ''
#                 except:
#                     CarsMake = ''
                
#                 try:
#                     if len(td_elements) == 15:
#                         CarsMakeModel = td_elements[2].text.strip()
#                     else:
#                         CarsMakeModel = ''
#                 except:
#                     CarsMakeModel = ''
                
#                 try:
#                     if len(td_elements) == 15:
#                         CarsMakeModelSeries = td_elements[3].text.strip()
#                     else:
#                         CarsMakeModelSeries = ''
#                 except:
#                     CarsMakeModelSeries = ''
            
#                 try:
#                     if len(td_elements) == 15:
#                         CarsPartNumber = td_elements[9].text.strip()
#                     else:
#                         CarsPartNumber = ''
#                 except:
#                     CarsPartNumber = ''
#                 # print(engine_cc, CarsMake, CarsMakeModel, CarsMakeModelSeries, CarsPartNumber)

#                 endless = {
#                     'Parttype (category)': makebrakerotor,
#                     'Parttype URL (category)': '',
#                     'Make': CarsMake,
#                     'Make URL': '',
#                     'Model': 'Model  ' +  CarsMakeModel,
#                     'Model URL': '',
#                     'Year':  '',
#                     'Series': CarsMakeModelSeries,
#                     'Engine cc': 'Engine cc  ' + engine_cc,
#                     'Type': '',
#                     'PartNumber': CarsPartNumber,
#                 }

#                 if CarsMake and CarsMakeModel and CarsMakeModelSeries and CarsPartNumber:
#                     data.append(endless)
#                     print('Saving', endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])


# brake_line = baseurl + '/products/suspension/index_functionxplus.html'
# r = requests.get(brake_line, headers=headers, verify=False)
# soup = BeautifulSoup(r.content, 'lxml')

# listbrake_line = soup.find('select', onchange='location.href=value;')

# itembrake_line = listbrake_line.find_all('option')[:2]
# linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]

# for listbrake_linelinks in linknameCarsbrake_line:
#     r = requests.get(listbrake_linelinks, headers=headers, verify=False)
#     soup = BeautifulSoup(r.content, 'lxml')
    
#     makesuspension = soup.find('div', 'maintitle_pc_box2').text.strip()
#     iframes = soup.find_all('iframe')

#     for iframe in iframes:
#         src = iframe['src']
#         iframe_content = requests.get(src).content
#         iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#         tables = iframe_soup.find_all('table')

#         for table in tables:
#             rows = table.find_all('tr')[7:]
#             for row in rows:
#                 td_elements = row.find_all('td')
#                 removetext = ['test']
#                 if any(text in td.text.strip() for td in td_elements for text in removetext):
#                     continue
#                 try:
#                     if len(td_elements) == 14:
#                         CarModel = td_elements[1].text.strip()
#                     else:
#                         CarModel = ''
#                 except:
#                     CarModel = ''

#                 try:
#                     if len(td_elements) == 14:
#                         CarSeries = td_elements[2].text.strip()
#                     else:
#                         CarSeries = ''
#                 except:
#                     CarSeries = ''

#                 try:
#                     if len(td_elements) == 14:
#                         partNumber = td_elements[3].text.strip()
#                     else:
#                         partNumber = ''
#                 except:
#                     partNumber = ''

#                 endless = {
#                     'Parttype (category)': 'サスペンション',
#                     'Parttype URL (category)': '',
#                     'Make': makesuspension,
#                     'Make URL': '',
#                     'Model':  CarModel,
#                     'Model URL': '',
#                     'Year':  '',
#                     'Series': CarSeries,
#                     'Engine cc': '',
#                     'Type': '',
#                     'PartNumber': partNumber,
#                 }

#                 if CarModel and CarSeries and partNumber:
#                     data.append(endless)
#                     print('Saving', endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['Series'], endless['PartNumber'])


# itembrake_line = listbrake_line.find_all('option')[2:]
# linknameCarsbrake_line = [option['value'] for option in itembrake_line if option.has_attr('value')]

# for listbrake_linelinks in linknameCarsbrake_line:
#     r = requests.get(listbrake_linelinks, headers=headers, verify=False)
#     soup = BeautifulSoup(r.content, 'lxml')
    
#     makesuspension = soup.find('div', 'maintitle_pc_box2').text.strip()
    
#     iframes = soup.find_all('iframe')

#     for iframe in iframes:
#         src = iframe['src']
#         iframe_content = requests.get(src).content
#         iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#         tables = iframe_soup.find_all('table')