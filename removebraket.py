import csv

# membuka file CSV
csv.field_size_limit(1000000000)
with open('', 'r') as csvfile:
    # membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # menambahkan kolom "VehicleRawProperties" pada header file CSV
    header = reader.fieldnames

    # membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # membaca setiap baris pada file CSV
    for row in reader:
        # mengambil nilai pada kolom "VehicleRawProperties"
        raw_vehicle_properties = row['VehicleRawProperties']

        # menghapus tanda "[" dan "]" dari nilai kolom "VehicleRawProperties"
        cleaned_raw_vehicle_properties = raw_vehicle_properties.replace('[{', '{').replace('}]', '}')

        # memperbarui nilai kolom "VehicleRawProperties" dengan nilai yang telah dihapus tanda "[" dan "]"
        row['VehicleRawProperties'] = cleaned_raw_vehicle_properties

        # menambahkan baris baru ke dalam list
        new_rows.append(row)

# menulis data baru ke dalam file CSV
with open('', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # menulis header file CSV
    writer.writeheader()

    # menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)
