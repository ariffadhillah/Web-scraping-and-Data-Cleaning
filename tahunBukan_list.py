# import csv
# import ast
# import re

# file_path = 'Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv'

# # Membaca file CSV
# csv.field_size_limit(1000000000)
# rows = []
# with open(file_path, 'r') as file:
#     reader = csv.DictReader(file)
#     fieldnames = reader.fieldnames
#     for row in reader:
#         rows.append(row)

# # Memproses data dan menambahkan properti baru
# for row in rows:
#     vehicle_raw_properties = ast.literal_eval(row['VehicleRawProperties'])

#     # Memeriksa tipe data
#     if isinstance(vehicle_raw_properties, tuple):
#         vehicle_raw_properties = vehicle_raw_properties[0]

#     others = vehicle_raw_properties.get('others', "")

#     # Mengambil tahun pertama dan tahun terakhir menggunakan ekspresi reguler
#     match = re.search(r'\b(\d{4})\b', others)
#     if match:
#         first_year = match.group(0)
#     else:
#         first_year = ''

#     match = re.findall(r'\b(\d{4})\b', others)
#     if match:
#         last_year = match[-1]
#     else:
#         last_year = ''

#     # Menambahkan properti baru "Years"
#     vehicle_raw_properties['Years'] = f"{first_year} - {last_year}"

#     # Mengubah ke format JSON
#     row['VehicleRawProperties'] = str(vehicle_raw_properties)

# # Menyimpan kembali ke file CSV
# with open(file_path, 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(rows)



import csv
import json

input_file = ""
output_file = ""
csv.field_size_limit(1000000000)
# Membaca file CSV
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Memproses dan memperbarui data
for row in rows:
    vehicle_properties = {}

    try:
        vehicle_properties = json.loads(row["VehicleRawProperties"])
    except json.JSONDecodeError:
        pass

    if "others" in vehicle_properties:
        others = vehicle_properties["others"]
        # Mencari tahun pertama dan terakhir dari properti "others"
        years = others.split()[0].strip()  # Tahun pertama
        if "-" in others:
            end_year = others.split("-")[1].split()[0].strip()  # Tahun terakhir
            years += " - " + end_year
        else:
            years += " - 0"

        # Menambahkan properti baru "Years" dengan rentang tahun yang ditemukan
        vehicle_properties["Years"] = years

    # Mengubah kembali ke format JSON
    row["VehicleRawProperties"] = json.dumps(vehicle_properties)

# Menulis kembali ke file CSV dengan format JSON
with open(output_file, "w", newline="") as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Data telah diperbarui dan disimpan dalam file CSV dengan format JSON.")
