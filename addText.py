import pandas as pd
import os

df = pd.read_csv('Data_Cleaning/hardrace.csv')

partNumber = df['PartNumber'].values.tolist()
rawVehicleProperties = df['List of Vehicle Compatibility'].values.tolist()
brand = df['Brand'].values.tolist()

# menghitung jumlah baris pada kolom 'RawVehicleProperties'
num_rows = len(partNumber)

# membuat DataFrame baru dengan kolom 'RawVehicleProperties', 'DataStandard', 'TypeId', 'ImportId', 'ImportTable', dan 'ImportRegion'
new_df = pd.DataFrame({"partnumber":partNumber,
                       'VehicleRawProperties': rawVehicleProperties, 
                       'VehicleDataStandard': ['0'] * num_rows, 
                       'TypeId': ['UVET1'] * num_rows, 
                       'ImportId': '', 
                       'ImportTable': ['bac_20233005_Hardrace'] * num_rows, 
                       'VehicleImportRegion': ['United Kingdom'] * num_rows,
                       'Brand': brand,
                       'UvdbFromYearID': '',
                       'UvdbToYearID':'',
                       'Action':['ADD'] * num_rows})

# membuat folder 'category_clean_data' jika belum ada
# if not os.path.exists('category_clean_data'):
#     os.makedirs('category_clean_data')

# menyimpan DataFrame baru ke dalam file csv dengan encoding utf-8
new_df.to_csv('', index=False, encoding='utf-8')
