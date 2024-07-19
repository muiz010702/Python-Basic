import numpy as np

# membuat matrix dengan tipe data tertentu
A = np.array(([1,2,3,4],[5,6,7,8]), dtype=float)

# membuat matrix dengan fungtion
def Matrix (baris, kolom):
    return kolom**2

def Jumlah (baris, kolom):
    return kolom + baris

B = np.fromfunction(Matrix, (1,5), dtype=int)
C = np.fromfunction(Jumlah, (4,4), dtype=int)

# membuat matrix dengan iterasi
iterasi = (M * M for M in range(8))
iterasiKali = (M * 2 for M in range(8))

D = np.fromiter(iterasiKali, dtype=int)

# Multiple Array
Mobil = [
    ('HRV',300.000),
    ('Kia Seltos', 450.000),
    ('Mazda CX5', 500.000)
]

print(B)
print(C)
print(D)
print(Mobil[2])