# # import requests
# # from bs4 import BeautifulSoup
# # import time

# # baseurl = 'https://www.endless-sport.co.jp'
# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# # }

# # processed_urls = set()
# # categoryProduct = []

# # pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

# # r = requests.get(pageBrakepads, headers=headers)
# # soup = BeautifulSoup(r.content, 'lxml')

# # listCarsName = []

# # brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
# # carList = brakepad_search_whole.find('div', id='right_menu_box')
# # for linkcars in carList.find_all('a', href=True):
# #     listCarsName.append(linkcars['href'])

# # productList = []
# # for carName in listCarsName:
# #     urlcar = requests.get(carName, headers=headers)
# #     soup = BeautifulSoup(urlcar.content, 'lxml')
# #     carNameIcons = soup.find_all('div', id='ewig_pad_whole')
# #     for itemCarName in carNameIcons:
# #         for href in itemCarName.find_all('a',  href=True):
# #             url = href['href']
# #             if url not in processed_urls:
# #                 productList.append(pageBrakepads.replace('/car_list.html', '/') + url)
# #                 processed_urls.add(url)
# #             # time.sleep(.5)
# #         print(productList)


# # # page 
# # importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
# # listImportedCar = []
# # for linkcarsimported in importedCar.find_all('a', href=True):
# #     listImportedCar.append(linkcarsimported['href'])
# # print(len(listImportedCar))
# # print(listImportedCar)



# import requests
# from bs4 import BeautifulSoup
# import time

# baseurl = 'https://www.endless-sport.co.jp'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
# }

# processed_urls = set()
# categoryProduct = set()

# pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

# r = requests.get(pageBrakepads, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# listCarsName = []

# brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
# carList = brakepad_search_whole.find('div', id='right_menu_box')
# for linkcars in carList.find_all('a', href=True):
#     listCarsName.append(linkcars['href'])

# productList = set()
# for carName in listCarsName:
#     urlcar = requests.get(carName, headers=headers)
#     soup = BeautifulSoup(urlcar.content, 'lxml')
#     carNameIcons = soup.find_all('div', id='ewig_pad_whole')
#     for itemCarName in carNameIcons:
#         for href in itemCarName.find_all('a',  href=True):
#             url = href['href']
#             if url not in processed_urls:
#                 productList.add(pageBrakepads.replace('/car_list.html', '/') + url)
#                 processed_urls.add(url)
#             # time.sleep(.5)
# print(list(productList))


# # page 
# importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
# listImportedCar = set()
# for linkcarsimported in importedCar.find_all('a', href=True):
#     listImportedCar.add(linkcarsimported['href'])
# print(len(listImportedCar))
# print(list(listImportedCar))


import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

processed_urls = set()
categoryProduct = []

pageBrakepads = baseurl + '/products/brake_pad/car_list.html'

r = requests.get(pageBrakepads, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listCarsName = []

brakepad_search_whole = soup.find('div', id='brakepad_search_whole')
carList = brakepad_search_whole.find('div', id='right_menu_box')
for linkcars in carList.find_all('a', href=True):
    listCarsName.append(linkcars['href'])

productList = []
for carName in listCarsName:
    urlcar = requests.get(carName, headers=headers)
    soup = BeautifulSoup(urlcar.content, 'lxml')
    carNameIcons = soup.find_all('div', id='ewig_pad_whole')
    for itemCarName in carNameIcons:
        for href in itemCarName.find_all('a',  href=True):
            # print(len(href))
            url = href['href']
            if url not in processed_urls:
                productList.append(pageBrakepads.replace('/car_list.html', '/') + url)
                processed_urls.add(url)
            # time.sleep(.5)
        print(len(productList))

# page 
importedCar = brakepad_search_whole.find_all('div', id='right_menu_box')[1]
listImportedCar = []
for linkcarsimported in importedCar.find_all('a', href=True):
    listImportedCar.append(linkcarsimported['href'])
# print(len(listImportedCar))
print(listImportedCar)

# # Save the URLs to a CSV file
# with open('urls.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=['url'])
#     writer.writeheader()
#     for url in productList + listImportedCar:
#         writer.writerow({'url': url})



