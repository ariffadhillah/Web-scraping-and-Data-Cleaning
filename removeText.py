import csv

csv.field_size_limit(1000000000)
with open('', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames
    new_rows = []
    
    for row in reader:
        vehicle_raw_properties = row['VehicleRawProperties']
        updated_properties = vehicle_raw_properties.replace('Petrol Engine', '').replace('Diesel', '')
        row['VehicleRawProperties'] = updated_properties
        new_rows.append(row)

# csv.field_size_limit(1000000000)        
with open('', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(new_rows)
