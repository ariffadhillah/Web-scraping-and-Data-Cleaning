import csv
import json
import re

csv.field_size_limit(1000000000)

with open('', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames + ['List of Years']
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
            years = re.findall(r'\d{4}', others)

            if len(years) > 1:
                start_year = int(years[0])
                end_year = int(years[1])
                years_range = list(range(start_year, end_year + 1))
                years_list = [str(year) for year in years_range]
                years_list = "', '".join(map(str, years_range))
                json_obj['List of Years'] = f"['{years_list}']"
            else:
                json_obj['List of Years'] = f"['{years[0]}']"

            vehicle_properties.append(json.dumps(json_obj))

        # Menggabungkan semua objek JSON menjadi satu string JSON
        # new_raw_vehicle_properties = json.dumps(vehicle_properties)
        new_raw_vehicle_properties = ', '.join(vehicle_properties)
        row['VehicleRawProperties'] = new_raw_vehicle_properties
        new_rows.append(row)

    with open('', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(new_rows)


















