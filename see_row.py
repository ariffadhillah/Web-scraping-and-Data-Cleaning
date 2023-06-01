import csv

# Membuka file CSV dengan encoding utf-8
csv.field_size_limit(1000000000)
with open('', 'r', encoding='utf-8') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Mencari baris yang memiliki nomor indeks 36134
    for idx, row in enumerate(reader):
        if idx == 36133:
            # Mencetak isi kolom dari baris tersebut
            for key, value in row.items():
                print(f"{key}: {value}")
            break


