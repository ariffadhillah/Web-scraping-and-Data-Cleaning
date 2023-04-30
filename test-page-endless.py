from translate import Translator
from bs4 import BeautifulSoup

html = '<h1 class="heading01--lv01 heading01">4輪用(CAR &amp; TRUCK)</h1>'
soup = BeautifulSoup(html, 'html.parser')
text_jp = soup.h1.text

translator = Translator(to_lang="en")
text_en = translator.translate(text_jp)

print(text_en)
