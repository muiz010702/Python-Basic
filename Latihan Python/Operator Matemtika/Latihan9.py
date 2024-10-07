"""
Tulis program untuk menghitung harga akhir setelah diskon. 
Jika harga barang p = 200000 dan diskon d = 20%, 
hitung total harga setelah diskon.
"""
p = 200000
d = 20
diskon = p * (d / 100)
Total = p - diskon
print("Harga mendapat potongan sebesar Rp.", diskon)
print("Harga setelah diskon adalah Rp.", Total)