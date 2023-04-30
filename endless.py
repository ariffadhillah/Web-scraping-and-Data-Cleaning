import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Mendapatkan halaman HTML dari URL
url = 'https://www.endless-sport.co.jp/products/products_index.html'
response = requests.get(url)
html = response.text

# Parsing HTML dengan BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
element = soup.find('div', class_='maintitle_pc_box2')

# Mendapatkan teks dalam bahasa Jepang
text_jp = element.text

# Menerjemahkan teks dari bahasa Jepang ke bahasa Inggris
translator = Translator()
text_en = translator.translate(text_jp, dest='en').text

# Mencetak hasil terjemahan
print(text_en)
