import csv
import json
import re

csv.field_size_limit(1000000000)
with open('', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames

    new_rows = []

    for row in reader:
        vehicle_raw_properties = row['VehicleRawProperties']
        
        # Mencari semua format JSON dalam kolom VehicleRawProperties
        json_matches = re.findall(r'{[^{}]*}', vehicle_raw_properties)

        if json_matches:
            # Mengambil data pertama dari format JSON
            first_json = json_matches[0]
            new_vehicle_raw_properties = first_json

            # Menyimpan data pertama kembali ke kolom VehicleRawProperties
            row['VehicleRawProperties'] = new_vehicle_raw_properties

        new_rows.append(row)

    with open('', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(new_rows)
