import requests
from bs4 import BeautifulSoup
import csv
import json
import time

from selectolax.parser import HTMLParser


def data_parse(response):
    html = HTMLParser(response.html)
    optiopns = html.css("ul#ui-id-10 > li")
    for  opt in optiopns:
        print(opt.attributes)


def main():
    url = "https://www.ferodo.com/catalogue.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    data_parse(soup)

if __name__ == "__main__":
    main()
