"""
Buatlah program yang meminta pengguna memasukkan dua angka. 
Program kemudian akan memeriksa apakah kedua angka tersebut sama atau tidak. 
Jika sama, tampilkan pesan "Angka pertama sama dengan angka kedua", 
jika tidak, tampilkan pesan "Angka pertama tidak sama dengan angka kedua".
"""

Angka1 = int(input("Masukan Angka Pertama:"))
Angka2 = int(input("Masukan angka kedua:"))

if Angka1 == Angka2:
    print("Angka pertama sama dengan angka kedua")
elif Angka1 != Angka2:
    print("Angka pertama tidak sama dengan angka kedua")
else:
    print("Angka tidak tersedia")