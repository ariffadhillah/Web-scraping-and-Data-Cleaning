import pandas as pd

# Membaca file CSV
df = pd.read_csv('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_file.csv')

# Menemukan baris-baris dengan data duplikat pada kolom "RawVehicleProperties"
duplicate_rows = df[df.duplicated(subset='RawVehicleProperties', keep=False)]

# Menampilkan jumlah baris yang merupakan duplikat
duplicate_count = len(duplicate_rows)

print("duplicate:", duplicate_count)




# # import pandas as pd

# # # Membaca file CSV
# # df = pd.read_csv('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_file.csv')

# # # Menghitung jumlah baris dalam kolom "RawVehicleProperties"
# # row_count = df['RawVehicleProperties'].count()

# # print("Jumlah baris:", row_count)



# import pandas as pd

# # Membaca file CSV
# df = pd.read_csv('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_file.csv')

# # Menghapus baris-baris duplikat berdasarkan kolom "RawVehicleProperties"
# df.drop_duplicates(subset='RawVehicleProperties', inplace=True)

# # Menyimpan DataFrame yang telah diubah ke dalam file CSV
# df.to_csv('Data_Cleaning/data/New-Data/automotivesuperstore_draft_vehicle_file.csv', index=False)
