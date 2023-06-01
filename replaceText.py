import pandas as pd
import json

# membaca data dari file CSV
data = pd.read_csv('')

# mengubah nilai "make" menjadi "name" dalam kolom "RawVehicleProperties"
data['VehicleRawProperties'] = data['VehicleRawProperties'].str.replace('"model"', '"Model"')

# Menyimpan data kembali ke dalam file CSV
data.to_csv('', index=False)
