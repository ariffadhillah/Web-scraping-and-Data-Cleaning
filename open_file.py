import pandas as pd

# membaca file csv
# pd.set_option('display.max_columns', 1000)
df = pd.read_csv('automotivesuperstore_exported.csv', nrows=50)
# menampilkan 1000 baris pertama dan semua kolom
print(df['Product Title'])
