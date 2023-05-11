import requests
from bs4 import BeautifulSoup
import csv
import time

baseurl = 'https://www.endless-sport.co.jp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

fields = ['Parttype (category)', 'Parttype URL (category)', 'Make', 'Make URL', 'Model', 'Model URL', 'Year', 'Engine cc', 'Type', 'PartNumber']
filename = 'Exemple-brake_rotor.csv'

data = []


processed_urls = set()


brake_rotor = baseurl + '/products/brake_rotor/index.html'

r = requests.get(brake_rotor, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# tekigou_icon

listbrakerotor = soup.find_all('div', class_='tekigou_icon')[1:]


listbrakerotorlinks = []

for itembrakerotor in listbrakerotor:
    for namecarslistbrakerotor in itembrakerotor.find_all('a', href=True):
        # print(namecarslistbrakerotor['href']) 
         listbrakerotorlinks.append(namecarslistbrakerotor['href']) 

for pagelistbrakerotor in listbrakerotorlinks:
    r = requests.get(pagelistbrakerotor, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    try:
        makebrakerotor = soup.find('div', 'maintitle_pc_box2').text.strip()
    except:
        makebrakerotor = ''
        
    divmodel = soup.find_all('div', class_='slidebox2')[1:]
        
    for div in divmodel:
        modelbrakerotor = div.text.strip() 
            
        iframesimport = div.find_next_sibling('div').find_all('iframe')
        for iframeimport in iframesimport:
            src = iframeimport['src']
            iframeimport_content = requests.get(src).content
            iframeimport_soup = BeautifulSoup(iframeimport_content, 'html.parser')
            tables = iframeimport_soup.find_all('table')

            for table in tables:
                partNumberbrakerotor = []
                rows = table.find_all('tr')[5:]
                # print(rows)
                for row in rows:
                    if row.has_attr('style') and 'height: 149px' in row['style'] and 'px' in row['style']:
                        continue
                    td_elements = row.find_all('td')
                    removetext = ['※ER154、155のディスクローター補修部品は、純正ブレーキローターの補修用としてはご使用いただけませんのでご注意ください。','※レガシィBE／BHは車種により装着できない場合がございます。車検証情報から適合調査をさせて頂きます。','※レガシィBL／BPは車種により装着できない場合がございます。車検証情報から適合調査をさせて頂きます。','※ディスク単体での販売となります。ベルハウジング及び固定ピンは純正をご使用ください。','	※レガシィBL／BPは車種により装着できない場合がございます。車検証情報から適合調査をさせて頂きます','※レガシィBE／BHは車種により装着できない場合がございます。車検証情報から適合調査をさせて頂きます','1PCSブレーキローター','2PCSブレーキローター','3PCSブレーキローター','※純正に比べ、厚みが25mmから26.5mmへ変更しております。ブレーキパッドのシムは外してからご使用ください','商品名','¥68,200','¥60,500','¥61,600','¥44,000','補修ブレーキローター','※純正ブレーキローターの寸法をご確認くださいませ。','¥36,300','¥66,000','※ベルハウジング及び固定ピンは純正を再使用してください。（固定用ボルト、ナットは付属します','¥52,800','¥30,800','¥38,500','※ベルハウジングの色はレーシングアルマイトとなります。色変更に関しては「ベルハウジングオーダーカラー」をご覧くださいませ','¥75,900','※ドリルドタイプのみとなります。','	※ベルハウジングはステンレス製でシルバーとなります。色変更はお受けしておりません','※リアドラム部はスチール製となります','※ASSYでの販売となります。','※本製品の販売につきましては、エンドレス認定ショップのみとなります。ご購入をご希望される方は、弊社までお問い合わせください。','※1 本製品の販売につきましては、生産を一時終了させていただいております。（詳しくはこちらをご覧くださいませ）','※ベルハウジングはステンレス製でシルバーとなります。色変更はお受けしておりません。','¥67,100','¥74,800','¥67,100','¥74,800' ,'¥67,000','¥73,700']
                    if any(text in td.text.strip() for td in td_elements for text in removetext):
                        continue 
                    try: 	
                        # partNumberbrakerotor = td_elements[1].text.strip()
                        if len(td_elements) < 12:
                            typebrakerotor = td_elements[1].text.strip()
                    
                        elif len(td_elements) < 4:
                            typebrakerotor = td_elements[1].text.strip()
                        else:
                            typebrakerotor = td_elements[1].text.strip()                    

                        if len(typebrakerotor) < 10:
                            typebrakerotor = td_elements[1].text.strip()
                            
                        
                        if len(td_elements) < 12:
                            partNumberbrakerotor = td_elements[2].text.strip()
                    
                        elif len(td_elements) < 4:
                            partNumberbrakerotor = td_elements[2].text.strip()
                        else:
                            partNumberbrakerotor = td_elements[2].text.strip()                    

                        if len(partNumberbrakerotor) < 10:
                            partNumberbrakerotor = td_elements[2].text.strip()
                            # continue
                        # print(partNumberbrakerotor)
                        if  partNumberbrakerotor and makebrakerotor and partNumberbrakerotor and typebrakerotor:
                            endless = {
                                'Parttype (category)': 'ブレーキローター',
                                'Parttype URL (category)': brake_rotor,
                                'Make': makebrakerotor,
                                'Make URL': pagelistbrakerotor,
                                'Model': modelbrakerotor,
                                'Model URL': pagelistbrakerotor,
                                'Year': '',
                                'Engine cc': '',
                                'Type': typebrakerotor,
                                'PartNumber': partNumberbrakerotor,
                            }
                            data.append(endless)
                            print('Saving',endless['Parttype (category)'], endless['Parttype URL (category)'], endless['Make'], endless['Make URL'], endless['Model'], endless['Model URL'], endless['Year'], endless['Engine cc'], endless['Type'], endless['PartNumber'])                    
                            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.DictWriter(csvfile, fieldnames=fields)
                                writer.writeheader()
                                for item in data:
                                    writer.writerow(item)
                    except:
                        None    

    # content_box = soup.find('div', class_='container')
    # for divmodel in content_box.find_all('div', class_='slidebox2'):
    #     divmodel

    #     print(divmodel.text.strip())
        

    



    # for containet in content_box
    # # print(divmodel)
    # print(divmodel)
    # try:
    # except:
    #     continue

    # for div in divmodel:
    #     model = div.h1.text.strip()
    #     enginecc = div.text.replace(model, '').strip()

    


