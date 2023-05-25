# # import csv
# # import re

# # # membuka file CSV
# # with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
# #     # membaca file CSV sebagai dictionary
# #     reader = csv.DictReader(csvfile)

# #     # menambahkan kolom "UvdbFromYearID" pada header file CSV
# #     header = reader.fieldnames + ['UvdbFromYearID']

# #     # membuat list kosong untuk menyimpan baris baru
# #     new_rows = []

# #     # membaca setiap baris pada file CSV
# #     for row in reader:
# #         # mengambil nilai pada kolom "VehicleRawProperties"
# #         vehicle_raw_properties = row['VehicleRawProperties']

# #         # mencari tahun pertama menggunakan regular expression pada key "others"
# #         match = re.search(r'\d{4}', vehicle_raw_properties.split("others")[-1])

# #         # jika match ditemukan, simpan tahun pertama pada kolom "UvdbFromYearID"
# #         if match:
# #             row['UvdbFromYearID'] = match.group(0)
# #         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID"
# #         else:
# #             row['UvdbFromYearID'] = ''

# #         # menambahkan baris baru ke dalam list
# #         new_rows.append(row)

# # # menulis data baru ke dalam file CSV
# # with open('data_new.csv', 'w', newline='') as csvfile:
# #     writer = csv.DictWriter(csvfile, fieldnames=header)

# #     # menulis header file CSV
# #     writer.writeheader()

# #     # menulis setiap baris baru ke dalam file CSV
# #     for row in new_rows:
# #         writer.writerow(row)





# import csv
# import re

# csv.field_size_limit(1000000000)

# # membuka file CSV
# with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # mencari tahun pertama menggunakan regular expression pada key "others"
#         match_from_year = re.search(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # jika match ditemukan, simpan tahun pertama pada kolom "UvdbFromYearID"
#         if match_from_year:
#             row['UvdbFromYearID'] = match_from_year.group(0)
#         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID"
#         else:
#             row['UvdbFromYearID'] = ''

#         # mencari tahun terakhir menggunakan regular expression pada key "others"
#         match_to_year = re.findall(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # jika match ditemukan, simpan tahun terakhir pada kolom "UvdbToYearID"
#         if match_to_year:
#             row['UvdbToYearID'] = match_to_year[-1]
#         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbToYearID"
#         else:
#             row['UvdbToYearID'] = ''

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)







import csv
import re

csv.field_size_limit(1000000000)

# Membuka file CSV
with open('', 'r') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Mengambil nilai pada kolom "VehicleRawProperties"
        vehicle_raw_properties = row['VehicleRawProperties']

        # Mencari tahun pertama menggunakan regular expression pada key "others"
        match_from_year = re.search(r'\d{4}', vehicle_raw_properties.split("others")[-1])

        # Jika match ditemukan, simpan tahun pertama pada kolom "UvdbFromYearID"
        if match_from_year:
            row['UvdbFromYearID'] = match_from_year.group(0)
        # Jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID"
        else:
            row['UvdbFromYearID'] = ''

        # Mencari tahun terakhir menggunakan regular expression pada key "others"
        match_to_year = re.findall(r'\d{4}', vehicle_raw_properties.split("others")[-1])

        # Jika match ditemukan, simpan tahun terakhir pada kolom "UvdbToYearID"
        if match_to_year:
            end_year = match_to_year[-1]
            # Jika tahun terakhir adalah "0", tampilkan "0" pada kolom "UvdbToYearID"
            if end_year == ' ':
                row['UvdbToYearID'] = '0'
            else:
                row['UvdbToYearID'] = end_year
        # Jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbToYearID"
        else:
            row['UvdbToYearID'] = ''

        # Menambahkan baris baru ke dalam list
        new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)

    # Menulis header file CSV
    writer.writeheader()

    # Menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)
