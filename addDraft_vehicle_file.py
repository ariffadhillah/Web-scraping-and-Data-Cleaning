import pandas as pd

# membaca file csv
df = pd.read_csv('Data_Cleaning/hardrace.csv')

# mengambil semua nilai dalam kolom 'partnumber' dan 'title'
# partnumber = df['PartNumber'].values.tolist()
partnumber = df['PartNumber'].values.tolist()
listofVehicleCompatibility = df['List of Vehicle Compatibility'].values.tolist()
brand = df['Brand'].values.tolist()


# automotivesuperstore_draft_vehicle_file


# membuat DataFrame baru dengan kolom 'newpartNumber', 'name product', dan 'WeightGrams'
new_df = pd.DataFrame({'partnumber': partnumber, 'VehicleRawProperties': listofVehicleCompatibility, 'VehicleDataStandard':'', 'TypeId':'', 'ImportId':'', 'ImportTable':'', 'VehicleImportRegion':'','Brand':brand, 'UvdbFromYearID':'','UvdbToYearID':'', 'Action':'' })

# menampilkan DataFrame baru
new_df.to_csv('Data_Cleaning/data/Hardrace_draft_vehicle_to_parts_file.csv', index=False, encoding='utf-8')






# import pandas as pd

# # membaca file csv
# df = pd.read_csv('')

# # mengambil semua nilai dalam kolom 'partnumber' dan 'title'
# partnumber = df['partnumber'].values.tolist()
# VehicleRawProperties = df['VehicleRawProperties'].values.tolist()
# VehicleDataStandard = df['VehicleDataStandard'].values.tolist()
# TypeId = df['TypeId'].values.tolist()
# ImportId = df['ImportId'].values.tolist()
# ImportTable = df['ImportTable'].values.tolist()
# VehicleImportRegion = df['VehicleImportRegion'].values.tolist()
# Brand = df['Brand'].values.tolist()
# UvdbFromYearID = df['UvdbFromYearID'].values.tolist()
# UvdbToYearID = df['UvdbToYearID'].values.tolist()
# Action = df['Action'].values.tolist()

# # membuat DataFrame baru dengan kolom 'newpartNumber', 'name product', dan 'WeightGrams'
# new_df = pd.DataFrame({'partnumber':partnumber, 'VehicleRawProperties':VehicleRawProperties, 'VehicleDataStandard':VehicleDataStandard,'TypeId': TypeId, 'ImportId':ImportId, 'ImportTable':ImportTable, 'VehicleImportRegion':VehicleImportRegion, 'Brand':Brand, 'UvdbFromYearID':UvdbFromYearID, 'UvdbToYearID':UvdbToYearID, 'Action':Action})

# # menampilkan DataFrame baru
# new_df.to_csv('', index=False, encoding='utf-8')
