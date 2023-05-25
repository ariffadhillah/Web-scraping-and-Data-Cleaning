import csv

# membuka file CSV
csv.field_size_limit(1000000000)
with open('', 'r', encoding='utf-8') as csvfile:
    # membaca file CSV sebagai list
    reader = list(csv.reader(csvfile))

    # mencari indeks kolom "VehicleRawProperties"
    header = reader[0]
    vehicle_raw_prop_index = header.index('List of Vehicle Compatibility')

    # membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # membaca setiap baris pada file CSV, kecuali header
    for row in reader[1:]:
        # memeriksa apakah nilai pada kolom "VehicleRawProperties" kosong atau hanya terdiri dari spasi
        if row[vehicle_raw_prop_index].strip() == "":
            # jika iya, lewati baris ini
            continue
        # jika tidak, tambahkan baris ke dalam list baru
        new_rows.append(row)

# menulis data baru ke dalam file CSV yang sama
with open('', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)

    # menulis header file CSV
    writer.writerow(header)

    # menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)
