import requests
from bs4 import BeautifulSoup


data = []


# urllist_braek_line_1 = [
# 'https://www.endless-sport.co.jp/products/brake_line/list_mitsubishi.html',
# 'https://www.endless-sport.co.jp/products/brake_line/list_honda.html'
# ]

# for url_braek_line in urllist_braek_line_1:
#     r = requests.get(url_braek_line)
#     soup = BeautifulSoup(r.content, 'lxml')

#     try:
#         makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
#     except:
#         makebraek_line = ' None'

#     divmodel = soup.find_all('div', class_='slidebox2')        
#     for div in divmodel:
#         modelbraek_line = div.text.strip()            
#         iframesimport = div.find_next_sibling('div').find_all('iframe')
#         for iframeimport in iframesimport:
#             src = iframeimport['src']
#             iframeimport_content = requests.get(src).content
#             iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#             tables = iframeimport_soup.find_all('table')
#             for table in tables:
#                 rows = table.find_all('tr')
#                 for row in rows:
#                     td_elementstype1 = row.find_all('td', class_='s7')
#                     if td_elementstype1:
#                         partNumberbraek_line = ' '.join(td_elementstype1[0].stripped_strings)
#                     else:
#                         partNumberbraek_line = None

#                     typebrakeline = None                
#                     td_elementstype = row.find_all('td', class_='s6')
#                     for idx, tdtypebrakeline in enumerate(td_elementstype):
#                         if tdtypebrakeline.has_attr('rowspan') and tdtypebrakeline['rowspan'] in ['4', '5', '6','8' ]:
#                             tdtypebrakeline.attrs['dir'] = 'ltr'
                    
#                             typebrakeline = ' '.join(tdtypebrakeline.stripped_strings)
#                     if not typebrakeline:
#                         continue
#                     if  makebraek_line and modelbraek_line and url_braek_line and typebrakeline and partNumberbraek_line:
#                         endless = {
#                             'Parttype (category)': '',
#                             'Parttype URL (category)': '',
#                             'Make': makebraek_line,
#                             'Make URL': '',
#                             'Model': modelbraek_line,
#                             'Model URL': url_braek_line,
#                             'Year': '',
#                             'Engine cc': '',
#                             'Type': typebrakeline,
#                             'PartNumber':partNumberbraek_line,
#                         }
#                         data.append(endless)
#                         print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber']) 

# urllist_braek_line_1 = [
# 'https://www.endless-sport.co.jp/products/brake_line/list_toyota.html',
# 'https://www.endless-sport.co.jp/products/brake_line/list_subaru.html',
# 'https://www.endless-sport.co.jp/products/brake_line/list_daihatsu.html'
# ]

# for url_braek_line in urllist_braek_line_1:
#     r = requests.get(url_braek_line)
#     soup = BeautifulSoup(r.content, 'lxml')

#     try:
#         makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
#     except:
#         makebraek_line = ' None'

#     divmodel = soup.find_all('div', class_='slidebox2')
        
#     for div in divmodel:
#         modelbraek_line = div.text.strip() 
            
#         iframesimport = div.find_next_sibling('div').find_all('iframe')
#         for iframeimport in iframesimport:
#             src = iframeimport['src']
#             iframeimport_content = requests.get(src).content
#             iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#             tables = iframeimport_soup.find_all('table')

#             for table in tables:
#                 rows = table.find_all('tr')

#                 for row in rows:
#                     partnumberbrakeline = row.find('td', class_='s8', rowspan="4")
#                     if partnumberbrakeline:
#                         partnumberbrakeline = partnumberbrakeline.text.strip()
#                     else:
#                         partnumberbrakeline = ""
#                     typebrakeline = None
#                     td_elements = row.find_all('td', class_='s7')

#                     for idx, tdtypebrakeline in enumerate(td_elements):
#                         if tdtypebrakeline.has_attr('rowspan') and tdtypebrakeline['rowspan'] in ['4', '5', '6' ]:
#                             tdtypebrakeline.attrs['dir'] = 'ltr'
#                             typebrakeline = ' '.join(tdtypebrakeline.stripped_strings)

#                     if not typebrakeline:
#                         continue
#                     if  makebraek_line and modelbraek_line and url_braek_line and typebrakeline and partnumberbrakeline:
#                         endless = {
#                             'Parttype (category)': '',
#                             'Parttype URL (category)': '',
#                             'Make': makebraek_line,
#                             'Make URL': '',
#                             'Model': modelbraek_line,
#                             'Model URL': '',
#                             'Year': '',
#                             'Engine cc': '',
#                             'Type': typebrakeline,
#                             'PartNumber':partnumberbrakeline,
#                         }
#                         data.append(endless)
#                         print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber']) 

# # # Madza
# list_mazda = 'https://www.endless-sport.co.jp/products/brake_line/list_mazda.html'
# r = requests.get(list_mazda)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
# except:
#     makebraek_line = ' None'

# divmodel = soup.find_all('div', class_='slidebox2')
    
# for div in divmodel:
#     modelbraek_line = div.text.strip() 
        
#     iframesimport = div.find_next_sibling('div').find_all('iframe')
#     for iframeimport in iframesimport:
#         src = iframeimport['src']
#         iframeimport_content = requests.get(src).content
#         iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#         tables = iframeimport_soup.find_all('table')

#         for table in tables:
#             rows = table.find_all('tr')

#             for row in rows:

#                 td_elementstype1 = row.find_all('td', class_='s6')
#                 if td_elementstype1:
#                     partNumberbraek_line = ' '.join(td_elementstype1[0].stripped_strings)
#                 else:
#                     partNumberbraek_line = None

#                 typebrakeline = None                
#                 td_elementstype = row.find_all('td', class_='s5')
#                 for idx, tdtypebrakeline in enumerate(td_elementstype):
#                     if tdtypebrakeline.has_attr('rowspan') and tdtypebrakeline['rowspan'] in ['4', '5', '6','8' ]:
#                         tdtypebrakeline.attrs['dir'] = 'ltr'                     
                
#                         typebrakeline = ' '.join(tdtypebrakeline.stripped_strings)

#                 if not typebrakeline:
#                     continue

#                 if  makebraek_line and modelbraek_line and list_mazda and typebrakeline and partNumberbraek_line:
#                     endless = {
#                         'Parttype (category)': '',
#                         'Parttype URL (category)': '',
#                         'Make': makebraek_line,
#                         'Make URL': '',
#                         'Model': modelbraek_line,
#                         'Model URL': list_mazda,
#                         'Year': '',
#                         'Engine cc': '',
#                         'Type': typebrakeline,
#                         'PartNumber':partNumberbraek_line,
#                     }
#                     data.append(endless)
#                     print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber']) 


# # # Madza
# list_lexus = 'https://www.endless-sport.co.jp/products/brake_line/list_lexus.html'
# r = requests.get(list_lexus)
# soup = BeautifulSoup(r.content, 'lxml')

# try:
#     makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
# except:
#     makebraek_line = ' None'

# divmodel = soup.find_all('div', class_='slidebox2')
    
# for div in divmodel:
#     modelbraek_line = div.text.strip() 
        
#     iframesimport = div.find_next_sibling('div').find_all('iframe')
#     for iframeimport in iframesimport:
#         src = iframeimport['src']
#         iframeimport_content = requests.get(src).content
#         iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#         tables = iframeimport_soup.find_all('table')

#         for table in tables:
#             rows = table.find_all('tr')

#             for row in rows:

#                 td_elementstype1 = row.find_all('td', class_='s4')
#                 if td_elementstype1:
#                     partNumberbraek_line = ' '.join(td_elementstype1[0].stripped_strings)
#                 else:
#                     partNumberbraek_line = None

#                 typebrakeline = None                
#                 td_elementstype = row.find_all('td', class_='s8')
#                 for idx, tdtypebrakeline in enumerate(td_elementstype):
#                     if tdtypebrakeline.has_attr('rowspan') and tdtypebrakeline['rowspan'] in ['4', '5', '6','8' ]:
#                         tdtypebrakeline.attrs['dir'] = 'ltr'                     
                
#                         typebrakeline = ' '.join(tdtypebrakeline.stripped_strings)

#                 if not typebrakeline:
#                     continue

#                 endless = {
#                     'Parttype (category)': '',
#                     'Parttype URL (category)': '',
#                     'Make': makebraek_line,
#                     'Make URL': '',
#                     'Model': modelbraek_line,
#                     'Model URL': list_lexus,
#                     'Year': '',
#                     'Engine cc': '',
#                     'Type': typebrakeline,
#                     'PartNumber':partNumberbraek_line,
#                 }
#                 data.append(endless)
#                 print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber']) 



# list_nissan = [
# 'https://www.endless-sport.co.jp/products/brake_line/list_nissan.html',
# 'https://www.endless-sport.co.jp/products/brake_line/list_suzuki.html'
# ]

# for url_braek_line in list_nissan:
#     r = requests.get(url_braek_line)
#     soup = BeautifulSoup(r.content, 'lxml')

#     try:
#         makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
#     except:
#         makebraek_line = ' None'

#     divmodel = soup.find_all('div', class_='slidebox2')
        
#     for div in divmodel:
#         modelbraek_line = div.text.strip() 
            
#         iframesimport = div.find_next_sibling('div').find_all('iframe')
#         for iframeimport in iframesimport:
#             src = iframeimport['src']
#             iframeimport_content = requests.get(src).content
#             iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
#             tables = iframeimport_soup.find_all('table')

#             for table in tables:
#                 rows = table.find_all('tr')

#                 for row in rows:
#                     partnumberbrakeline = None
#                     td_elements = row.find_all('td', class_='s8')
#                     for idx, tdpartnumberbrakeline in enumerate(td_elements):
#                         if tdpartnumberbrakeline.has_attr('rowspan') and tdpartnumberbrakeline['rowspan'] in ['3','4', '5', '6', '8']:
#                             tdpartnumberbrakeline.attrs['dir'] = 'ltr'
#                             partnumberbrakeline = ' '.join(tdpartnumberbrakeline.stripped_strings)
#                             break  

#                     if not partnumberbrakeline:
#                         continue

#                     tdtypebrakeline = None
#                     td_elements = row.find_all('td', class_='s7')
#                     for idx, tdtypebrakeline in enumerate(td_elements):
#                         if tdtypebrakeline.has_attr('rowspan') and tdtypebrakeline['rowspan'] in ['3', '4', '5', '6' ,'8']:
#                             tdtypebrakeline.attrs['dir'] = 'ltr'
#                             typebrakeline = ' '.join(tdtypebrakeline.stripped_strings)

#                     if not typebrakeline:
#                         continue


#                     if  makebraek_line and modelbraek_line and url_braek_line and typebrakeline and partnumberbrakeline:
#                         endless = {
#                             'Parttype (category)': '',
#                             'Parttype URL (category)': '',
#                             'Make': makebraek_line,
#                             'Make URL': '',
#                             'Model': modelbraek_line,
#                             'Model URL': '',
#                             'Year': '',
#                             'Engine cc': '',
#                             'Type': typebrakeline,
#                             'PartNumber':partnumberbrakeline,
#                         }
#                         data.append(endless)
#                         print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber']) 







list_braek_line_import = 'https://www.endless-sport.co.jp/products/brake_line/list_import.html'
r = requests.get(list_braek_line_import)
soup = BeautifulSoup(r.content, 'lxml')

try:
    makebraek_line = soup.find('div', class_='maintitle_pc_box2').text.strip()
except:
    makebraek_line = ' None'

divmodel = soup.find_all('div', class_='slidebox2')
        
for div in divmodel:
    modelbraek_line = div.text.strip() 
            
    iframesimport = div.find_next_sibling('div').find_all('iframe')
    for iframeimport in iframesimport:
        src = iframeimport['src']
        iframeimport_content = requests.get(src).content
        iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
        tables = iframeimport_soup.find_all('table')

        for table in tables:
            rows = table.find_all('tr')[3:]
            for row in rows:
                element_yers = row.find_all('td')
                removetext = ['モデル', '品番']
                if any(text in td.text.strip() for td in element_yers for text in removetext):
                    continue 

                year = element_yers
                # engine = row.find_all('td')
                # type_ = row.find_all('td')
                # PartNumberFront = row.find_all('td')
                # PartNumberRear = row.find_all('td')[13:]
                # if PartNumberFront and PartNumberRear:
                #     PartNumber = PartNumberFront[4].text.strip() +' '+ PartNumberRear[0].text.strip()
                # else:
                #     PartNumber = ""                            

                if year :
                    endless = {
                        'Parttype (category)': '',
                        'Parttype URL (category)': '',
                        'Make': '',
                        'Make URL': '',
                        'Model': '',
                        'Model URL': '',
                        'Year': year[2].text.strip(),
                        'Engine cc':'',
                        'Type': '',
                        'PartNumber':'',
                    }
                    data.append(endless)
                    print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])






















# # ///////////////////////////////////////////////////////////

# # import requests
# # from bs4 import BeautifulSoup

# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

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
#     print(makebraek_line)

#     iframes = soup.find_all('iframe')
#     for iframe in iframes:
#         src = iframe['src']
#         iframe_content = requests.get(src).content
#         iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#         tables = iframe_soup.find_all('table')
        

        




# import requests
# from bs4 import BeautifulSoup

# # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_subaru.html'

# testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_toyota.html' 
# # # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_lexus.html'
# # # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_lexus.html'
# # # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_honda.html'
# # # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_mazda.html'
# # # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_mitsubishi.html'
# # # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_subaru.html'
# # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_subaru.html'
# # testModel = 'https://www.endless-sport.co.jp/products/brake_line/list_daihatsu.html'


# r = requests.get(testModel)
# soup = BeautifulSoup(r.content, 'lxml')

# data = []

# try:
#     makebrakeline = soup.find('div', class_='maintitle_pc_box2').text.strip()
# except:
#     makebrakeline = 'None'

# divmodels = soup.find_all('div', class_='slidebox2')

# for div in divmodels:
#     modelbrakerotor = div.text.strip()
#     iframes = div.find_next_sibling('div').find_all('iframe')
#     for iframe in iframes:
#         src = iframe['src']
#         iframe_content = requests.get(src).content
#         iframe_soup = BeautifulSoup(iframe_content, 'html.parser')
#         tables = iframe_soup.find_all('table')

#         for table in tables:
#             rows = table.find_all('tr')

#             for row in rows:
#                 td_elements = row.find_all('td', class_='s7', rowspan="4")
#                 print(td_elements)
               
#                 # if len(td_elements) > 2:
#                 #     ftd_element = td_elements
#                 #     print(ftd_element)

