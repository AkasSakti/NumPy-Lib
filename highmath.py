import numpy as np

# Contoh data
data = np.array([12, 15, 21, 29, 45, 55, 62, 70, 85, 95])

# STATISTIK DASAR
print("Data:", data)

# Menghitung rata-rata (mean)
mean = np.mean(data)
print(f"Rata-rata (Mean): {mean}")

# Menghitung median
median = np.median(data)
print(f"Median: {median}")

# Menghitung standar deviasi (standard deviation)
std_dev = np.std(data)
print(f"Standar Deviasi (Standard Deviation): {std_dev}")

# Menghitung varians (variance)
variance = np.var(data)
print(f"Varians (Variance): {variance}")

# TRIGONOMETRI
# Membuat array sudut dalam derajat
sudut_derajat = np.array([0, 30, 45, 60, 90])
print("\nSudut dalam derajat:", sudut_derajat)

# Mengonversi derajat ke radian
sudut_radian = np.radians(sudut_derajat)
print("Sudut dalam radian:", sudut_radian)

# Menghitung nilai sinus
sinus = np.sin(sudut_radian)
print("Sinus:", sinus)

# Menghitung nilai cosinus
cosinus = np.cos(sudut_radian)
print("Cosinus:", cosinus)

# Menghitung nilai tangen
tangen = np.tan(sudut_radian)
print("Tangen:", tangen)
