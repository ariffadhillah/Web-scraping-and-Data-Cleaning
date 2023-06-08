import pandas as pd

# membaca file csv
df = pd.read_csv('Data_Cleaning/nrf/NRF.csv')

# mengambil semua nilai dalam kolom 'partnumber' dan 'title'

partnumber = df['PartNumber'].values.tolist()
rawVehicleProperties = df['Product Title'].values.tolist()


# membuat DataFrame baru dengan kolom 'newpartNumber', 'name product', dan 'WeightGrams'
new_df = pd.DataFrame({'partnumber':partnumber,'VehicleRawProperties':rawVehicleProperties, 'VehicleDataStandard':'','TypeId':'','ImportId':'','ImportTable':'','VehicleImportRegion':'','UvdbFromYearID':'','UvdbToYearID':'','Action':''})

# menampilkan DataFrame baru
new_df.to_csv('Data_Cleaning/nrf/Nrf_draft_vehicle_to_parts_file.csv', index=False, encoding='utf-8')

