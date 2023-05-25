import csv
import json
import re

# membuka file CSV
csv.field_size_limit(1000000000)
with open('', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames
    new_rows = []

    for row in reader:
        raw_vehicle_properties = row['VehicleRawProperties']
        vehicle_properties = []

        # Mencari semua format JSON dalam baris VehicleRawProperties
        json_matches = re.findall(r'{[^{}]*}', raw_vehicle_properties)

        for json_match in json_matches:
            try:
                json_obj = json.loads(json_match)
            except json.JSONDecodeError:
                continue
            
            others = json_obj.get('others', '')
            updated_others = re.sub(r'\d{4}', '', others).strip()
            json_obj['others'] = updated_others

            vehicle_properties.append(json.dumps(json_obj))

        # Menggabungkan semua objek JSON menjadi satu string JSON
        new_raw_vehicle_properties = ', '.join(vehicle_properties)
        row['VehicleRawProperties'] = new_raw_vehicle_properties
        new_rows.append(row)

    with open('', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(new_rows)
