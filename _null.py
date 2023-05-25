import csv

# Membuka file CSV
with open('', 'r') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Mengambil nilai pada kolom "UvdbToYearID"
        uvdb_to_year_id = row['UvdbToYearID']

        # Memeriksa jika nilai adalah "0", mengubahnya menjadi "null"
        if uvdb_to_year_id == '0':
            row['UvdbToYearID'] = 'null'

        # Menambahkan baris baru ke dalam list
        new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)

    # Menulis header file CSV
    writer.writeheader()

    # Menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)
