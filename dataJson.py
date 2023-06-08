import csv
import json

# Membuka file CSV
with open('', 'r') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Menambahkan kolom "format_data" pada header file CSV
    header = reader.fieldnames + ['format_data']

    # Membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Mengambil nilai pada kolom "VehicleRawProperties"
        vehicle_raw_properties = row['VehicleRawProperties']

        # Membagi nilai pada kolom "VehicleRawProperties" menjadi bagian-bagian terpisah
        parts = vehicle_raw_properties.split(' ')

        # Membuat format data dalam bentuk JSON
        format_data = {
            'make': parts[0].strip(),
            'model': '',
            'engine': ''
        }

        # Menyimpan bagian-bagian selanjutnya ke dalam format data
        if len(parts) > 1:
            format_data['model'] = parts[1].strip()
        if len(parts) > 2:
            format_data['engine'] = parts[2].strip()

        # Mengubah format data menjadi JSON
        format_data_json = json.dumps(format_data)

        # Menyimpan format data pada kolom "format_data"
        row['format_data'] = format_data_json

        # Menambahkan baris baru ke dalam list
        new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('Data_Cleaning/nrf/Nrf_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Menulis header file CSV
    writer.writeheader()

    # Menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)

print("Data berhasil diubah menjadi format JSON, dan kolom 'format_data' telah diperbarui.")
