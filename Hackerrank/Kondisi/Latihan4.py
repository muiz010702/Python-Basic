"""
Buatlah program yang meminta pengguna memasukkan usia mereka. 
Program kemudian akan memeriksa apakah usia tersebut termasuk kategori anak-anak (usia kurang dari 12), 
remaja (usia 12 hingga 17), 
dewasa (usia 18 hingga 64), atau lansia (usia 65 ke atas). Tampilkan kategori yang sesuai.
"""

Usia = int(input("Usia saya:"))
if Usia < 12:
    print("Anak Anak")
elif Usia in range (12, 17):
    print("Remaja")
elif Usia in range (18, 64):
    print("Dewasa")
elif Usia > 65:
    print("Lansia")