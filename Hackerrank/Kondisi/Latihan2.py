"""
Buatlah program yang meminta pengguna memasukkan sebuah angka. 
Program kemudian akan memeriksa apakah angka tersebut lebih besar dari 10 atau tidak. 
Jika lebih besar dari 10, tampilkan pesan "Angka lebih besar dari 10", 
jika tidak, tampilkan pesan "Angka kurang dari atau sama dengan 10".
"""

Angka = int(input("Masukkan angka: "))

if Angka == 10:
  print("Angka yg dimasukan sama")
elif Angka > 10:
  print("Angka lebih besar dari 10")
else:
  print("Angka kurang dari atau sama dengan 10")
  
