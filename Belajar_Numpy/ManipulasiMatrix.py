import numpy as np 

Angka = np. array((
                    [5,4,3],
                    [3,7,6]))

print("===================================")
print("matris angka dengan ukuran", Angka.shape)
print(Angka)

print("===================================")

# Transpose Matrix
print("ini adalah tranpose matrix")
print(Angka.transpose()) # cara 1
print(np.transpose(Angka)) # cara 2

print("===================================")

# flatten vektor atau vektor baris
print("ini adalah vektor baris")
print(Angka.ravel()) # cara 1
print(np.ravel(Angka)) # cara 2

print("===================================")

# reshape matrix
print("ini adalah reshape matrix")
print(Angka.reshape(3,2)) # cara 1

print("===================================")

# resize matrix
print("ini adalah resize matrix")
Angka.resize(3,2)
print(Angka) # cara 1

print("===================================")

print("matris angka dengan ukuran", Angka.shape)

