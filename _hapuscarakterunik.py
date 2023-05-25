import csv

# Membuka file CSV input
with open('', 'r') as input_file:
    reader = csv.DictReader(input_file)
    header = reader.fieldnames

    # Membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Memeriksa apakah kolom "TypeId" tidak kosong
        if row['TypeId'].strip():  # Menambahkan strip() untuk menghapus whitespace yang tidak terlihat
            new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('', 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(new_rows)
