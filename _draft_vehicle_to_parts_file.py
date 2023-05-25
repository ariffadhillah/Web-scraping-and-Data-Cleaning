import pandas as pd

# membaca file csv
df = pd.read_csv('Data_Cleaning/data/file_product_automotivesuperstore_exported.csv')

# mengambil semua nilai dalam kolom 'partnumber' dan 'title'
partnumber = df['PartNumber'].values.tolist()
ListofVehicleCompatibility = df['List of Vehicle Compatibility'].values.tolist()
Brand = df['Brand'].values.tolist()



# membuat DataFrame baru dengan kolom 'newpartNumber', 'name product', dan 'WeightGrams'
new_df = pd.DataFrame({'partnumber':partnumber, 'VehicleRawProperties':ListofVehicleCompatibility, 'VehicleDataStandard':'', 'TypeId':'', 'ImportId':'','ImportTable':'', 'VehicleImportRegion':'','Brand':Brand, 'UvdbFromYearID':'', 'UvdbToYearID':'', 'Action':''})

# menampilkan DataFrame baru
new_df.to_csv('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_to_parts_file.csv', index=False, encoding='utf-8')

