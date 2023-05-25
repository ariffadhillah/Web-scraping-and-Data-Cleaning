import requests
from bs4 import BeautifulSoup
from tkinter import *

# Fungsi untuk menampilkan pop-up
def show_popup():
    popup_window = Toplevel(root)
    popup_window.title("Pop-up Window")
    popup_window.geometry("400x300")

    # Mendapatkan URL pop-up dari atribut onclick
    popup_url = td_element['onclick'].split("'")[1]

    # Kirim permintaan GET ke URL pop-up
    response = requests.get(popup_url)
    html = response.text

    # Tampilkan HTML pop-up pada label
    popup_label = Label(popup_window, text=html)
    popup_label.pack()

# URL halaman utama
url = 'https://www.denso.com/cgi-bin/plug/4wplug/4wjp_data.cgi?name=%e3%82%a2%e3%82%b9%e3%82%ab&filename=maker1jpn.txt&m=0'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', class_='search_table')

# Mencari elemen <td> dengan teks "IK16"
td_element = table.find('td', string='IK16')

if td_element:
    # Membuat tombol yang akan menampilkan pop-up saat diklik
    root = Tk()
    button = Button(root, text="IK16", command=show_popup)
    button.pack()
    root.mainloop()
else:
    print("Elemen <td> tidak ditemukan.")
