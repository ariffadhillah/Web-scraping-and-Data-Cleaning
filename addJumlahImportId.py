
import csv

# membuka file CSV
csv.field_size_limit(1000000000)
with open('', 'r') as csvfile:
    # membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # menambahkan kolom "ImportId" pada header file CSV
    header = reader.fieldnames

    # membuat list kosong untuk menyimpan baris baru
    new_rows = []
# 6981
    # menghitung jumlah baris dalam kolom "RawVehicleProperties"
    row_count = 1
    for row in reader:
        raw_vehicle_properties = row['RawVehicleProperties']
        if raw_vehicle_properties:
            row['ImportId'] = str(row_count)
            row_count += 1
            new_rows.append(row)

# menulis data baru ke dalam file CSV
with open('', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # menulis header file CSV
    writer.writeheader()

    # menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)