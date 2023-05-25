import csv
import re

csv.field_size_limit(1000000000)

# Membuka file CSV
with open('', 'r') as csvfile:
    # Membaca file CSV sebagai dictionary
    reader = csv.DictReader(csvfile)

    # Membuat list kosong untuk menyimpan baris baru
    new_rows = []

    # Membaca setiap baris pada file CSV
    for row in reader:
        # Mengambil nilai pada kolom "VehicleRawProperties"
        vehicle_raw_properties = row['VehicleRawProperties']

        # Mencari nilai "others" menggunakan regular expression
        match_others = re.search(r'"others"\s*:\s*"([^"]+)"', vehicle_raw_properties)

        # Jika match ditemukan
        if match_others:
            others = match_others.group(1)
            years = re.findall(r'\d{4}', others)

            # Jika ditemukan tahun pertama dan tahun terakhir
            if len(years) > 1:
                start_year = years[0]
                end_year = years[1]
                years_range = f"{start_year} - {end_year}"
            # Jika hanya ditemukan tahun pertama
            elif len(years) == 1:
                start_year = years[0]
                end_year = '0'
                years_range = f"{start_year} - {end_year}"
            # Jika tidak ditemukan tahun
            else:
                years_range = ''

            row['UvdbFromYearID'] = start_year
            row['UvdbToYearID'] = end_year
        # Jika match tidak ditemukan
        else:
            row['UvdbFromYearID'] = ''
            row['UvdbToYearID'] = ''

        # Menambahkan baris baru ke dalam list
        new_rows.append(row)

# Menulis data baru ke dalam file CSV
with open('D', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)

    # Menulis header file CSV
    writer.writeheader()

    # Menulis setiap baris baru ke dalam file CSV
    for row in new_rows:
        writer.writerow(row)
