import numpy as np
import pandas as pd

# Membaca file Excel
data = pd.ExcelFile('Dataset_Studi_Kasus.xlsx')

# Membaca lembar kerja untuk masing-masing dataset
pemasukan_bulanan = pd.read_excel(data, sheet_name='Pemasukan Bulanan')

# Mengambil data pemasukan sebagai array
pemasukan_array = pemasukan_bulanan['Pemasukan'].values

# Menghitung rata-rata pemasukan
rata_rata_pemasukan = np.mean(pemasukan_array)
print(f'Rata-rata Pemasukan: {rata_rata_pemasukan}')

# Menghitung total pemasukan
total_pemasukan = np.sum(pemasukan_array)
print(f'Total Pemasukan: {total_pemasukan}')

# Menghitung standar deviasi pemasukan
std_dev_pemasukan = np.std(pemasukan_array)
print(f'Standar Deviasi Pemasukan: {std_dev_pemasukan}')

# Mencari pemasukan tertinggi dan terendah
pemasukan_tertinggi = np.max(pemasukan_array)
pemasukan_terendah = np.min(pemasukan_array)
print(f'Pemasukan Tertinggi: {pemasukan_tertinggi}')
print(f'Pemasukan Terendah: {pemasukan_terendah}')

# Mencari bulan dengan pemasukan tertinggi dan terendah
bulan_tertinggi = pemasukan_bulanan['Bulan'].iloc[np.argmax(pemasukan_array)]
bulan_terendah = pemasukan_bulanan['Bulan'].iloc[np.argmin(pemasukan_array)]
print(f'Bulan dengan Pemasukan Tertinggi: {bulan_tertinggi}')
print(f'Bulan dengan Pemasukan Terendah: {bulan_terendah}')
