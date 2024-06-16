# contoh 1
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

# variabel global dan lokal
# 1. variabel global
a = 20

def add(b):
    result = a+b
    return result

bilanganPertama = add(5)
print(bilanganPertama)

# 2. variabel lokal
def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)