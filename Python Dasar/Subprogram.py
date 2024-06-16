#belajar subprogram
# contoh 1
Lebar = 10
panjang = 15

Luas_Persegi = Lebar * panjang
print(Luas_Persegi)

Lebar = 5
panjang = 12

Luas_Persegi = Lebar * panjang
print(Luas_Persegi)

# contoh 2
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)