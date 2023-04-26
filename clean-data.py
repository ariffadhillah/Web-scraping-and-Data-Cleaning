# # data tahu pertama

# import pandas as pd
# import csv
# # Load data dari file CSV dengan encoding ISO-8859-1
# df = pd.read_csv('stanceduk_draft_vehicle_to_parts_file.csv', encoding='ISO-8859-1')

# # Memisahkan tahun dari kolom "VehicleRawProperties" menggunakan regex
# df['UvdbFromYearID'] = df['VehicleRawProperties'].str.extract(r'(\d{4})')
  
# # Menyimpan hasilnya ke file Excel
# df.to_csv('coba.csv', index=False)




# # ambil data tahun pertama dan tahun terakhir
# import pandas as pd

# # Load data dari file CSV dengan encoding ISO-8859-1
# df = pd.read_csv('data-reformat-clean.csv', encoding='ISO-8859-1')

# # Memisahkan tahun awal dan akhir dari kolom "VehicleRawProperties" menggunakan regex
# df[['UvdbFromYearID', 'UvdbToYearID']] = df['VehicleRawProperties'].str.extract(r'(\d{4})\s*-\s*(\d{4})?')

# # Jika tahun akhir tidak ada, maka diganti dengan tahun awal
# df['UvdbToYearID'] = df['UvdbToYearID'].fillna(df['UvdbFromYearID'])

# # Menyimpan hasilnya ke file CSV
# df.to_csv('stanceduk_draft_vehicle_to_parts_file.csv', index=False)



# import pandas as pd

# # Load data dari file CSV dengan encoding ISO-8859-1
# df = pd.read_csv('data-reformat-clean.csv', encoding='ISO-8859-1')

# # Memisahkan tahun awal dan akhir dari kolom "VehicleRawProperties" menggunakan regex
# df[['UvdbFromYearID', 'UvdbToYearID']] = df['VehicleRawProperties'].str.extract(r'(\d{4})\s*-\s*(\d{4})?')

# # Ubah nilai pada kolom 'UvdbToYearID' menjadi kosong jika tidak ada tahun akhir yang terdeteksi pada kolom 'VehicleRawProperties'
# df['UvdbToYearID'] = df['UvdbToYearID'].where(df['UvdbToYearID'].notnull(), '')

# # Menyimpan hasilnya ke file CSV
# df.to_csv('stanceduk_draft_vehicle_to_parts_file.csv', index=False)


# benar

# import pandas as pd

# # Load data dari file CSV dengan encoding ISO-8859-1
# df = pd.read_csv('data-reformat-clean.csv', encoding='ISO-8859-1')

# # Memisahkan tahun awal dan akhir dari kolom "VehicleRawProperties" menggunakan regex
# df[['UvdbFromYearID', 'UvdbToYearID']] = df['VehicleRawProperties'].str.extract(r'(\d{4})\s*-\s*(\d{4})?')

# # Ubah nilai pada kolom 'UvdbToYearID' menjadi kosong jika tidak ada tahun akhir yang terdeteksi pada kolom 'VehicleRawProperties'
# df['UvdbToYearID'] = df['UvdbToYearID'].where(df['UvdbToYearID'].notnull(), '')

# # Menyimpan hasilnya ke file CSV
# df.to_csv('stanceduk_draft_vehicle_to_parts_file.csv', index=False)



import csv
import json

# Baca file CSV dan tulis ke dalam list
with open('stanceduk_draft_vehicle_file.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Tambahkan properti 'name' pada setiap objek di dalam kolom 'VehicleRawProperties'
for row in rows:
    vehicle_raw_properties = json.loads(row['RawVehicleProperties'])
    model_name = list(vehicle_raw_properties.keys())[0]
    model_desc = vehicle_raw_properties[model_name]
    vehicle_properties = {'name': f"{model_name} {model_desc}"}
    row['RawVehicleProperties'] = json.dumps(vehicle_properties)

# Simpan data yang sudah diubah ke dalam file CSV
with open('stanceduk_draft_vehicle_file.csv', mode='w', newline='') as f:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


