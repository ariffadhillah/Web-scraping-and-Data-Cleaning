# import pandas as pd

# # membaca file csv
# df = pd.read_csv('category/automotivesuperstore.csv')

# # mengambil semua nilai dalam kolom 'partnumber' dan 'title'
# partnumber = df['PartNumber'].values.tolist()
# VehicleRawProperties = df['List of Vehicle Compatibility'].values.tolist()
# brand = df['Brand'].values.tolist()

# # "Category (Parent)","Category URL (Parent)","Category - Leaf (Child 1)","Category URL - Leaf (Child 1)","Product URL","PartNumber","Product Title","Product Subtitle","Product Description","Image URLs","Price","List of Vehicle Compatibility","Brand","OE number / cross-reference","Others","Other_fitment"


# # membuat DataFrame baru dengan kolom 'newpartNumber', 'name product', dan 'WeightGrams'
# new_df = pd.DataFrame({'partnumber': partnumber,'VehicleRawProperties':VehicleRawProperties , 'VehicleDataStandard':'','TypeId':'', 'ImportId':'', 'ImportTable':'', 'VehicleImportRegion':'', 'Brand': brand, 'UvdbFromYearID':'', 'UvdbToYearID':'', 'Action': ''  })

# # menampilkan DataFrame baru
# new_df.to_csv('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', index=False, encoding='utf-8')



# import pandas as pd
# import os

# df = pd.read_csv('category/automotivesuperstore.csv')

# rawVehicleProperties = df['List of Vehicle Compatibility'].values.tolist()


# new_df = pd.DataFrame({'RawVehicleProperties': rawVehicleProperties, 'DataStandard':'', 'TypeId':'', 'ImportId':'','ImportTable':'', 'ImportRegion' :'' })


# # membuat folder 'category' jika belum ada
# if not os.path.exists('category_clean_data'):
#     os.makedirs('category_clean_data')

# # menyimpan DataFrame baru ke dalam file csv dengan encoding utf-8
# new_df.to_csv('category_clean_data/automotivesuperstore_draft_vehicle_file.csv', index=False, encoding='utf-8')



# import pandas as pd
# import os

# df = pd.read_csv('category/automotivesuperstore.csv')

# partNumber = df['PartNumber'].values.tolist()
# rawVehicleProperties = df['List of Vehicle Compatibility'].values.tolist()
# brand = df['Brand'].values.tolist()

# # menghitung jumlah baris pada kolom 'RawVehicleProperties'
# num_rows = len(partNumber)

# # membuat DataFrame baru dengan kolom 'RawVehicleProperties', 'DataStandard', 'TypeId', 'ImportId', 'ImportTable', dan 'ImportRegion'
# new_df = pd.DataFrame({"partnumber":partNumber,
#                        'VehicleRawProperties': rawVehicleProperties, 
#                        'VehicleDataStandard': ['0'] * num_rows, 
#                        'TypeId': ['UVET1'] * num_rows, 
#                        'ImportId': list(range(1, num_rows+1)), 
#                        'ImportTable': ['bac_20231405_Automotivesuperstore'] * num_rows, 
#                        'VehicleImportRegion': ['Australia'] * num_rows,
#                        'Brand': brand,
#                        'UvdbFromYearID': '',
#                        'UvdbToYearID':'',
#                        'Action':['ADD'] * num_rows})

# # membuat folder 'category_clean_data' jika belum ada
# if not os.path.exists('category_clean_data'):
#     os.makedirs('category_clean_data')

# # menyimpan DataFrame baru ke dalam file csv dengan encoding utf-8
# new_df.to_csv('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', index=False, encoding='utf-8')





# import pandas as pd
# import json

# # membaca data dari file CSV
# data = pd.read_csv('category_clean_data/automotivesuperstore_draft_vehicle_file.csv')

# try:
#     # loop melalui setiap item dan mengubah kunci "make" menjadi "name"
#     for i, row in data.iterrows():
#         category_clean_data = json.loads(row['RawVehicleProperties'])
#         for item in category_clean_data:
#             item['name'] = item.pop('make')
#         data.at[i, 'RawVehicleProperties'] = json.dumps(category_clean_data)
# except:
#     None

# make

# import pandas as pd
# import json

# # membaca data dari file CSV
# data = pd.read_csv('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv')

# # mengubah nilai "make" menjadi "name" dalam kolom "RawVehicleProperties"
# data['VehicleRawProperties'] = data['VehicleRawProperties'].str.replace('model', 'Model')

# # Menyimpan data kembali ke dalam file CSV
# data.to_csv('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', index=False)



# import csv
# import re

# # membuka file CSV
# csv.field_size_limit(1000000000)
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "UvdbFromYearID" pada header file CSV
#     header = reader.fieldnames + ['UvdbFromYearID']

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mencari tahun pertama menggunakan regular expression
#         match = re.search(r'\d{4}', row['VehicleRawProperties'])

#         # jika match ditemukan, simpan tahun pertama pada kolom "UvdbFromYearID"
#         if match:
#             row['UvdbFromYearID'] = match.group(0)
#         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID"
#         else:
#             row['UvdbFromYearID'] = '  '

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('data_new.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)




# import pandas as pd
# import json
# df = pd.read_csv('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', usecols=['UvdbToYearID'], nrows=1000)

# values = df['UvdbToYearID'].values.tolist()

# # Menampilkan nilai dari 50 baris pertama
# for value in values:
#     print(value)

# # row['UvdbFromYearID'] = ''
# #             row['UvdbToYearID'] = ''



# import csv
# import re

# csv.field_size_limit(1000000000)
# # membuka file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "UvdbFromYearID" pada header file CSV
#     header = reader.fieldnames + ['UvdbFromYearID']

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # mencari tahun pertama menggunakan regular expression pada key "others"
#         match = re.search(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # jika match ditemukan, simpan tahun pertama pada kolom "UvdbFromYearID"
#         if match:
#             row['UvdbFromYearID'] = match.group(0)
#         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID"
#         else:
#             row['UvdbFromYearID'] = ''

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('data_new.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)



# import csv
# import re

# csv.field_size_limit(1000000000)
# # membuka file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "UvdbFromYearID" dan "UvdbToYearID" pada header file CSV
#     header = reader.fieldnames + ['UvdbFromYearID', 'UvdbToYearID']

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # mencari tahun pertama menggunakan regular expression pada key "others"
#         match_from = re.search(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # mencari tahun terakhir menggunakan regular expression pada key "others"
#         match_to = re.search(r'\d{4}(?=[^0-9]*$)', vehicle_raw_properties.split("others")[-1])

#         # jika match_from dan match_to ditemukan, simpan tahun pada kolom "UvdbFromYearID" dan "UvdbToYearID"
#         if match_from and match_to:
#             row['UvdbFromYearID'] = match_from.group(0)
#             row['UvdbToYearID'] = match_to.group(0)
#         # jika hanya match_from yang ditemukan, simpan tahun pada kolom "UvdbFromYearID" dan nilai kosong pada kolom "UvdbToYearID"
#         elif match_from:
#             row['UvdbFromYearID'] = match_from.group(0)
#             row['UvdbToYearID'] = ''
#         # jika hanya match_to yang ditemukan, simpan tahun pada kolom "UvdbToYearID" dan nilai kosong pada kolom "UvdbFromYearID"
#         elif match_to:
#             row['UvdbFromYearID'] = ''
#             row['UvdbToYearID'] = match_to.group(0)
#         # jika tidak ada match ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID" dan "UvdbToYearID"
#         else:
#             row['UvdbFromYearID'] = ''
#             row['UvdbToYearID'] = ''

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('data_new.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)


# import csv
# import re

# csv.field_size_limit(1000000000)
# # membuka file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "UvdbFromYearID" dan "UvdbToYearID" pada header file CSV
#     header = reader.fieldnames + ['UvdbFromYearID', 'UvdbToYearID']

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # mencari tahun pertama menggunakan regular expression pada key "others"
#         match_from = re.search(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # mencari tahun terakhir menggunakan regular expression pada key "others"
#         match_to = re.search(r'\d{4}(?=[^0-9]*$)', vehicle_raw_properties.split("others")[-1])

#         # jika match_from dan match_to ditemukan, simpan tahun pada kolom "UvdbFromYearID" dan "UvdbToYearID"
#         if match_from and match_to:
#             row['UvdbFromYearID'] = match_from.group(0)
#             row['UvdbToYearID'] = match_to.group(0)
#         # jika hanya match_from yang ditemukan, simpan tahun pada kolom "UvdbFromYearID" dan nilai kosong pada kolom "UvdbToYearID"
#         elif match_from:
#             row['UvdbFromYearID'] = match_from.group(0)
#             row['UvdbToYearID'] = ''
#         # jika hanya match_to yang ditemukan, simpan tahun pada kolom "UvdbToYearID" dan nilai kosong pada kolom "UvdbFromYearID"
#         elif match_to:
#             row['UvdbFromYearID'] = ''
#             row['UvdbToYearID'] = match_to.group(0)
#         # jika tidak ada match ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID" dan "UvdbToYearID"
#         else:
#             row['UvdbFromYearID'] = ''
#             row['UvdbToYearID'] = ''

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('exampledatayears.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)



# import csv
# import re

# csv.field_size_limit(1000000000)
# # membuka file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "UvdbFromYearID" dan "UvdbToYearID" pada header file CSV
#     header = reader.fieldnames + ['UvdbFromYearID', 'UvdbToYearID']

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # mencari tahun pertama dan terakhir menggunakan regular expression pada key "others"
#         match = re.findall(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # jika match ditemukan, simpan tahun pertama pada kolom "UvdbFromYearID" dan tahun terakhir pada kolom "UvdbToYearID"
#         if match:
#             row['UvdbFromYearID'] = match[0]
#             row['UvdbToYearID'] = match[-1]
#         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbFromYearID" dan "UvdbToYearID"
#         else:
#             row['UvdbFromYearID'] = ''
#             row['UvdbToYearID'] = ''

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('data_new.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)



# import csv
# import re

# csv.field_size_limit(1000000000)

# # membuka file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'r') as csvfile:
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
#             row['UvdbFromYearID'] = '  '

#         # mencari tahun terakhir menggunakan regular expression pada key "others"
#         match_to_year = re.findall(r'\d{4}', vehicle_raw_properties.split("others")[-1])

#         # jika match ditemukan, simpan tahun terakhir pada kolom "UvdbToYearID"
#         if match_to_year:
#             row['UvdbToYearID'] = match_to_year[-1]
#         # jika match tidak ditemukan, simpan nilai kosong pada kolom "UvdbToYearID"
#         else:
#             row['UvdbToYearID'] = '  '

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file_modife.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)








# menghapus baris yang kosong

# import csv

# # membuka file CSV
# csv.field_size_limit(1000000000)
# with open('category_clean_data/automotivesuperstore_draft_vehicle_file.csv', 'r', encoding='utf-8') as csvfile:
#     # membaca file CSV sebagai list
#     reader = list(csv.reader(csvfile))

#     # mencari indeks kolom "VehicleRawProperties"
#     header = reader[0]
#     vehicle_raw_prop_index = header.index('RawVehicleProperties')

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV, kecuali header
#     for row in reader[1:]:
#         # memeriksa apakah nilai pada kolom "VehicleRawProperties" kosong atau hanya terdiri dari spasi
#         if row[vehicle_raw_prop_index].strip() == "":
#             # jika iya, lewati baris ini
#             continue
#         # jika tidak, tambahkan baris ke dalam list baru
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV yang sama
# with open('category_clean_data/automotivesuperstore_draft_vehicle_file.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)

#     # menulis header file CSV
#     writer.writerow(header)

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)



# memeriksa kolom



# mengambil data sekitar 600 baris

import pandas as pd

# memuat file csv dan mengambil 4000 baris pertama
df = pd.read_csv('', nrows=7000)

# menyimpan 4000 baris ke dalam file csv baru
df.to_csv('', index=False)


# import csv

# # Membuka file CSV input
# with open('category/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as input_file:
#     reader = csv.reader(input_file)
#     header = next(reader)
    
#     # Memeriksa apakah "List of Years" ada dalam header
#     if 'List of Years' in header:
#         header.remove('List of Years')

#     # Menulis data baru ke dalam file CSV tanpa kolom "List of Years"
#     with open('category/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as output_file:
#         writer = csv.writer(output_file)
        
#         # Menulis header baru tanpa kolom "List of Years"
#         writer.writerow(header)

#         # Menyalin data baris per baris tanpa kolom "List of Years"
#         for row in reader:
#             if 'List of Years' in header:
#                 del row[header.index('List of Years')]
#             writer.writerow(row)






# import csv
# import json

# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     header = reader.fieldnames
#     new_rows = []

#     for row in reader:
#         vehicle_raw_properties = row['VehicleRawProperties']
#         if vehicle_raw_properties:
#             vehicle_properties = json.loads(vehicle_raw_properties)
#             if 'List of Years' in vehicle_properties:
#                 years = vehicle_properties['List of Years']
#                 years_str = json.dumps(years)
#                 vehicle_properties['List of Years'] = years_str
#             row['VehicleRawProperties'] = json.dumps(vehicle_properties)
#         new_rows.append(row)

# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(new_rows)



# memperbaiki key 
# import csv
# import json

# # Membuka file CSV
# csv.field_size_limit(1000000000)
# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r', encoding='utf-8') as csvfile:
#     # Membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # Menyimpan nama kolom header
#     header = reader.fieldnames

#     # Membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # Membaca setiap baris pada file CSV
#     for row in reader:
#         # Mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # Mengubah nilai key "List of Years" dengan menambahkan tanda kutip ganda setelah titik dua
#         vehicle_raw_properties_dict = json.loads(vehicle_raw_properties)
#         if 'List of Years' in vehicle_raw_properties_dict:
#             years = vehicle_raw_properties_dict['List of Years']
#             years_with_quotes = json.dumps(years)

#             # Memperbarui nilai kolom "VehicleRawProperties" dengan nilai yang baru
#             vehicle_raw_properties_dict['List of Years'] = years_with_quotes
#             row['VehicleRawProperties'] = json.dumps(vehicle_raw_properties_dict)

#         # Menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # Menulis data baru ke dalam file CSV
# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # Menulis header file CSV
#     writer.writeheader()

#     # Menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)




# import csv
# import json
# import re

# # membuka file CSV
# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "List of Years" pada header file CSV
#     header = reader.fieldnames

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "VehicleRawProperties"
#         vehicle_raw_properties = row['VehicleRawProperties']

#         # mengubah teks JSON yang tidak valid menjadi objek Python
#         try:
#             vehicle_properties = json.loads(vehicle_raw_properties)
#         except json.JSONDecodeError:
#             # jika teks JSON tidak valid, lewati baris ini
#             continue

#         # menghapus tahun dari key "others"
#         others = vehicle_properties.get('others', '')
#         updated_others = re.sub(r'\d{4}\s*-\s*\d{4}', '', others).strip()

#         # memperbarui nilai key "others"
#         vehicle_properties['others'] = updated_others

#         # mengubah kembali objek Python menjadi teks JSON yang valid
#         new_vehicle_raw_properties = json.dumps(vehicle_properties)

#         # memperbarui nilai kolom "VehicleRawProperties" dengan teks JSON yang telah diubah
#         row['VehicleRawProperties'] = new_vehicle_raw_properties

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)





# import csv
# import json
# import re

# # membuka file CSV
# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "List of Years" pada header file CSV
#     header = reader.fieldnames + ['List of Years']

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "RawVehicleProperties"
#         raw_vehicle_properties = row['VehicleRawProperties']

#         # mengubah teks JSON yang tidak valid menjadi objek Python
#         try:
#             vehicle_properties = json.loads(raw_vehicle_properties)
#         except json.JSONDecodeError:
#             # jika teks JSON tidak valid, lewati baris ini
#             continue

#         # mengambil nilai tahun dari key "others"
#         others = vehicle_properties.get('others', '')
#         years = re.findall(r'\d{4}', others)

#         # menambahkan data tahun ke dalam key "List of Years"
#         vehicle_properties['List of Years'] = years

#         # mengubah kembali objek Python menjadi teks JSON yang valid
#         new_raw_vehicle_properties = json.dumps(vehicle_properties)

#         # memperbarui nilai kolom "RawVehicleProperties" dengan teks JSON yang telah diubah
#         row['VehicleRawProperties'] = new_raw_vehicle_properties

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('category/Example-automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)




# import pandas as pd
# import json
# df = pd.read_csv('category_clean_data/automotivesuperstore_product_file.csv', usecols=['sku'], nrows=100)

# values = df['sku'].values.tolist()

# # Menampilkan nilai dari 50 baris pertama
# for value in values:
#     print(value)




# import csv

# # membuka file CSV
# csv.field_size_limit(1000000000)
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "ImportId" pada header file CSV
#     header = reader.fieldnames

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # menghitung jumlah baris dalam kolom "RawVehicleProperties"
#     row_count = 1
#     for row in reader:
#         raw_vehicle_properties = row['VehicleRawProperties']
#         if raw_vehicle_properties:
#             row['ImportId'] = str(row_count)
#             row_count += 1
#             new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)


















# import csv

# # membuka file CSV
# csv.field_size_limit(1000000000)
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'r') as csvfile:
#     # membaca file CSV sebagai dictionary
#     reader = csv.DictReader(csvfile)

#     # menambahkan kolom "RawVehicleProperties" pada header file CSV
#     header = reader.fieldnames

#     # membuat list kosong untuk menyimpan baris baru
#     new_rows = []

#     # membaca setiap baris pada file CSV
#     for row in reader:
#         # mengambil nilai pada kolom "RawVehicleProperties"
#         raw_vehicle_properties = row['VehicleRawProperties']

#         # menghapus tanda "[" dan "]" dari nilai kolom "RawVehicleProperties"
#         cleaned_raw_vehicle_properties = raw_vehicle_properties.replace('[', '').replace(']', '')

#         # memperbarui nilai kolom "RawVehicleProperties" dengan nilai yang telah dihapus tanda "[" dan "]"
#         row['VehicleRawProperties'] = cleaned_raw_vehicle_properties

#         # menambahkan baris baru ke dalam list
#         new_rows.append(row)

# # menulis data baru ke dalam file CSV
# with open('category_clean_data/automotivesuperstore_draft_vehicle_to_parts_file.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)

#     # menulis header file CSV
#     writer.writeheader()

#     # menulis setiap baris baru ke dalam file CSV
#     for row in new_rows:
#         writer.writerow(row)
