# import csv
# import re

# # Membuka file CSV
# with open('Data_Cleaning/nrf/Nrf_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     # Membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # Menambahkan kolom "Years" pada header file CSV
#     header = reader.fieldnames + ['Years']

#     # Membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # Membaca setiap baris pada file CSV
#     for row in reader:
#         # Mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # Mencari tahun menggunakan regular expression
#         match = re.search(r'(\d{2,4})-', vehicle_raw_properties)

#         # Mengambil tahun pertama
#         if match:
#             year = match.group(1)
#             # Mengubah format tahun menjadi 4 digit angka
#             if len(year) == 2:
#                 if int(year) < 50:
#                     year = '20' + year
#                 else:
#                     year = '19' + year
#         else:
#             year = ""

#         # Menyimpan tahun pada kolom "Years"
#         row['Years'] = year

#         # Menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # Menulis data baru ke dalam file CSV
# with open('Data_Cleaning/nrf/Nrf_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # Menulis header file CSV
#     writer.writeheader()

#     # Menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)

# print("Tahun berhasil diambil dan disimpan dalam kolom 'Years'.")





import csv
import re

# Membuka file CSV
with open('', 'r') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Menambahkan kolom "Years" pada header file CSV
    header = reader.fieldnames + ['Years']

    # Membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Mengambil nilai pada kolom "VehicleRawProperties"
        vehicle_raw_properties = row['VehicleRawProperties']

        # Mencari tahun menggunakan regular expression
        match = re.search(r'(\d{2,4})-', vehicle_raw_properties)

        # Mengambil tahun pertama
        if match:
            year = match.group(1)
            # Mengubah format tahun menjadi 4 digit angka
            if len(year) == 2:
                if int(year) < 50:
                    year = '20' + year
                else:
                    year = '19' + year
            # Menghapus tahun dari kolom "VehicleRawProperties"
            vehicle_raw_properties = re.sub(r'(\d{2,4})-', '', vehicle_raw_properties)
        else:
            year = ""

        # Menyimpan tahun pada kolom "Years"
        row['Years'] = year
        # Menyimpan hasil penghapusan tahun pada kolom "VehicleRawProperties"
        row['VehicleRawProperties'] = vehicle_raw_properties

        # Menambahkan baris baru ke dalam list
        new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Menulis header file CSV
    writer.writeheader()

    # Menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)

print("Tahun berhasil diambil, kolom 'Years' dan 'VehicleRawProperties' telah diperbarui.")
