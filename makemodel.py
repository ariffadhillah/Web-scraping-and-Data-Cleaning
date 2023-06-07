import csv

# Membuka file CSV
with open('Data_Cleaning/endless/endless-raw.csv', 'r', encoding='utf-8') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Membuat list untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Menggabungkan nilai dari kolom "Make", "Model", dan "Type" menjadi kolom "Name"
        name = f"{row['Make']} {row['Model']} {row['Type']}"
        row['Name'] = name

        # Menambahkan baris baru ke dalam list
        new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('Data_Cleaning/endless/test.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Mendefinisikan fieldnames berdasarkan header dari file CSV
    fieldnames = reader.fieldnames + ['Name']

    # Menulis data baru ke dalam file CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)

print("Data berhasil digabungkan dan disimpan ke file.")
