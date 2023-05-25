
# # import csv
# # import json
# # import re

# # csv.field_size_limit(1000000000)

# # with open('', 'r') as csvfile:
# #     reader = csv.DictReader(csvfile)
# #     header = reader.fieldnames + ['Years']
# #     new_rows = []

# #     for row in reader:
# #         raw_vehicle_properties = row['VehicleRawProperties']
# #         vehicle_properties = []

# #         # Mencari semua format JSON dalam baris VehicleRawProperties
# #         json_matches = re.findall(r'{[^{}]*}', raw_vehicle_properties)

# #         for json_match in json_matches:
# #             try:
# #                 json_obj = json.loads(json_match)
# #             except json.JSONDecodeError:
# #                 continue
            
# #             others = json_obj.get('others', '')
# #             years = re.findall(r'\d{4}', others)

# #             if len(years) > 1:
# #                 start_year = int(years[0])
# #                 end_year = int(years[1])
# #                 years_range = f"{start_year} - {end_year}"
# #                 json_obj['Years'] = years_range
# #             else:
# #                 json_obj['Years'] = years[0]

# #             vehicle_properties.append(json.dumps(json_obj))

# #         # Menggabungkan semua objek JSON menjadi satu string JSON
# #         new_raw_vehicle_properties = ', '.join(vehicle_properties)
# #         row['VehicleRawProperties'] = new_raw_vehicle_properties
# #         new_rows.append(row)

# #     with open('', 'w', newline='') as csvfile:
# #         writer = csv.DictWriter(csvfile, fieldnames=header)
# #         writer.writeheader()
# #         writer.writerows(new_rows)






# import csv
# import json
# import re

# csv.field_size_limit(1000000000)

# with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     header = reader.fieldnames + ['Years']
#     new_rows = []

#     for row in reader:
#         raw_vehicle_properties = row['VehicleRawProperties']
#         vehicle_properties = []

#         # Mencari semua format JSON dalam baris VehicleRawProperties
#         json_matches = re.findall(r'{[^{}]*}', raw_vehicle_properties)

#         for json_match in json_matches:
#             try:
#                 json_obj = json.loads(json_match)
#             except json.JSONDecodeError:
#                 continue

#             others = json_obj.get('others', '')
#             years = re.findall(r'\d{4}', others)

#             if len(years) > 0:
#                 if len(years) > 1 and years[-1] == '0':
#                     years_range = f"{years[0]} - 0"
#                 else:
#                     years_range = ' - '.join(years)
#                 json_obj['Years'] = years_range

#             vehicle_properties.append(json.dumps(json_obj))

#         # Menggabungkan semua objek JSON menjadi satu string JSON
#         new_raw_vehicle_properties = ', '.join(vehicle_properties)
#         row['VehicleRawProperties'] = new_raw_vehicle_properties
#         new_rows.append(row)

#     with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=header)
#         writer.writeheader()
#         writer.writerows(new_rows)





import csv
import json
import re

csv.field_size_limit(1000000000)

with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames + ['Years']
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

            if len(years) > 0:
                if len(years) > 1:
                    start_year = years[0]
                    end_year = years[1] if years[1] != '0' else '0'
                    years_range = f"{start_year} - {end_year}"
                else:
                    years_range = years[0]

                json_obj['Years'] = years_range

            vehicle_properties.append(json.dumps(json_obj))

        # Menggabungkan semua objek JSON menjadi satu string JSON
        new_raw_vehicle_properties = ', '.join(vehicle_properties)
        row['VehicleRawProperties'] = new_raw_vehicle_properties
        new_rows.append(row)

    with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(new_rows)
