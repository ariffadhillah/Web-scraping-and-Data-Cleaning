import csv

# Membuka file CSV dengan menggunakan encoding utf-8
csv.field_size_limit(1000000000)
with open('', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames

    # Membuat list kosong untuk menyimpan baris yang telah diperbaiki
    new_rows = []

    # Iterasi setiap baris pada file CSV
    for row in reader:
        product_description = row['Product Description']

        # Periksa apakah kolom "Product Description" kosong atau hanya terdiri dari spasi
        if product_description.strip():
            # Perbaiki struktur teks dalam kolom "Product Description"
            product_description = '\n'.join(line.strip() for line in product_description.split('\n') if line.strip())

            # Simpan baris yang telah diperbaiki ke dalam struktur data baru
            row['Product Description'] = product_description
            new_rows.append(row)

# Tulis struktur data baru ke file CSV
with open('', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(new_rows)
