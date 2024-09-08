import numpy as np

# Membuat array 1D
array_1d = np.array([1, 2, 3])
print("Array 1D:")
print(array_1d)

# Membuat matriks 2D (array 2D)
matriks_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatriks 2D:")
print(matriks_2d)

# Operasi penjumlahan elemen-elemen array dan matriks
print("\nPenjumlahan Array 1D dengan skalar 5:")
print(array_1d + 5)

print("\nPenjumlahan Matriks 2D dengan matriks lain:")
matriks_lain = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matriks_2d + matriks_lain)

# Operasi perkalian elemen-elemen array dan matriks
print("\nPerkalian Array 1D dengan skalar 2:")
print(array_1d * 2)

print("\nPerkalian Matriks 2D dengan matriks lain (elemen per elemen):")
print(matriks_2d * matriks_lain)

# Operasi perkalian matriks (dot product)
print("\nPerkalian matriks 2D (dot product):")
print(np.dot(matriks_2d, matriks_lain))

# Transposisi matriks
print("\nTransposisi Matriks 2D:")
print(np.transpose(matriks_2d))
