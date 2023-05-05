import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}
processed_urls = set()

# Page Brake pads
brake_caliper = baseurl + '/products/brake_caliper/index.html'


r = requests.get(brake_caliper, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listCarsName = []
listImportedCar = []
data = []
list_Brake_caliper = []

links_index2 = []
linkModel = []
leftmenuindex1 = soup.find('div', id='leftmenu_index2')
# for brakeCaliper in leftmenuindex1:
for urlCarsList in leftmenuindex1.find_all('a', href=True):
    links_index2.append(urlCarsList['href'])

for crasListBrakeCaliper in links_index2:
    r = requests.get(crasListBrakeCaliper, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    listCarsBrakeCaliper = soup.find_all('div', id='maker_icons')
    
    for listMake in listCarsBrakeCaliper:
        for linkMake in listMake.find_all('a', href=True):
            linkModel.append(linkMake['href'])

for linkMake in linkModel:
    r = requests.get(linkMake, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    test = soup.find('div', class_='maintitle_pc_box2')
    print(test.text.strip())