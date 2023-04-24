# # data tahu pertama

# import pandas as pd
# import csv
# # Load data dari file CSV dengan encoding ISO-8859-1
# df = pd.read_csv('stanceduk_draft_vehicle_to_parts_file.csv', encoding='ISO-8859-1')

# # Memisahkan tahun dari kolom "VehicleRawProperties" menggunakan regex
# df['UvdbFromYearID'] = df['VehicleRawProperties'].str.extract(r'(\d{4})')
  
# # Menyimpan hasilnya ke file Excel
# df.to_csv('coba.csv', index=False)




# ambil data tahun pertama dan tahun terakhir
import pandas as pd

# Load data dari file CSV dengan encoding ISO-8859-1
df = pd.read_csv('stanceduk_draft_vehicle_to_parts_file.csv', encoding='ISO-8859-1')

# Memisahkan tahun awal dan akhir dari kolom "VehicleRawProperties" menggunakan regex
df[['UvdbFromYearID', 'UvdbToYearID']] = df['VehicleRawProperties'].str.extract(r'(\d{4})\s*-\s*(\d{4})?')

# Jika tahun akhir tidak ada, maka diganti dengan tahun awal
df['UvdbToYearID'] = df['UvdbToYearID'].fillna(df['UvdbFromYearID'])

# Menyimpan hasilnya ke file CSV
df.to_csv('hasil.csv', index=False)

