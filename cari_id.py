import csv

# Membaca file automotivesuperstore_draft_vehicle_file.csv dan memetakan RawVehicleProperties ke ImportId
vehicle_data = {}
with open('', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        raw_vehicle_properties = row['RawVehicleProperties']
        import_id = row['ImportId']
        vehicle_data[raw_vehicle_properties] = import_id

# Membaca file automotivesuperstore_draft_vehicle_to_parts_file.csv dan mencocokkan dengan vehicle_data
new_rows = []
with open('Data_Cleaning/Hardrace_draft_vehicle_to_parts_file.csv', 'r') as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames

    for row in reader:
        vehicle_raw_properties = row['VehicleRawProperties']
        if vehicle_raw_properties in vehicle_data:
            row['ImportId'] = vehicle_data[vehicle_raw_properties]
        new_rows.append(row)

# Menyimpan hasil ke dalam file automotivesuperstore_draft_vehicle_to_parts_file_sama_id.csv
with open('Data_Cleaning/Hardrace_draft_vehicle_to_parts_file.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(new_rows)
