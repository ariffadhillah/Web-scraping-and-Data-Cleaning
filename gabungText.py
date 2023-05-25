import csv

# membuka file CSV
csv.field_size_limit(1000000000)
with open('', 'r', encoding='latin1') as csvfile:
    # membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # menambahkan kolom "UvdbFromYearID" pada header file CSV
    header = reader.fieldnames

    # membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # membaca setiap baris pada file CSV
    for row in reader:
        # mengambil nilai pada kolom "Brand" dan "sku"
        brand = row['Brand']
        sku = row['sku']

        # menggabungkan nilai dari kolom "Brand" dan "sku"
        new_sku = sku + '-' + brand

        # memperbarui nilai kolom "sku" dengan nilai yang baru
        row['sku'] = new_sku

        # menambahkan baris baru ke dalam list
        new_rows.append(row)

# menulis data baru ke dalam file CSV
with open('Data_Cleaning/data/automotivesuperstore_product_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # menulis header file CSV
    writer.writeheader()

    # menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)
