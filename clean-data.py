# data tahu pertama

import pandas as pd
import csv
# Load data dari file CSV dengan encoding ISO-8859-1
df = pd.read_csv('stanceduk_draft_vehicle_to_parts_file.csv', encoding='ISO-8859-1')

# Memisahkan tahun dari kolom "VehicleRawProperties" menggunakan regex
df['UvdbFromYearID'] = df['VehicleRawProperties'].str.extract(r'(\d{4})')
  
# Menyimpan hasilnya ke file Excel
df.to_csv('coba.csv', index=False)

