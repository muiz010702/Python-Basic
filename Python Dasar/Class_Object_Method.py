# belajar class, object, dan mthod

# A. CLASS
# membuat class Mobil
class Mobil:
    warna = 'Hijau' # ini adalah atribut

# B. OBJECT
Mobil_x = Mobil() # memanggil class mobil
# mengubah atribut atau objek 
Mobil_x.warna = 'Biru'
print(Mobil_x.warna) # mencetak sebuah class yang diikuti dengan atributnya 

# C. ATRIBUTE
class merek:
    Jenis = 'Honda'

Motor1 = merek()
print(Motor1.Jenis)

Motor2 = merek()
print(Motor2.Jenis)

# mengubah atribut atau objek 
Motor1.Jenis = 'Sujuki'

print(Motor1.Jenis)
print(Motor2.Jenis)

#D. CLASS INSTRUCTOR
"""
Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python 
yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas.
"""

# a. latihan 1
class Merek:
    # Atribut Instance
    def __init__(self):  
        self.Jenis = 'Honda'

Motor1 = Merek()
Motor2 = Merek()

# mencetak atribute 
print(Motor1.Jenis)  # Akan mencetak 'Honda'
print(Motor2.Jenis)  # Akan mencetak 'Honda' 

Motor1.Jenis = 'Yamaha'
# mencetak atribute kembali
print(Motor1.Jenis)  # Akan mencetak 'Yamaha'
print(Motor2.Jenis)  # Akan mencetak 'Honda'

# b. latihan 2
class merek:
    def __init__(self, Warna, kecepatan, Jenis, Nama) -> None:
        self.Jenis = Jenis
        self.Warna = Warna
        self.Kecepatan = kecepatan
        self.Nama = Nama
Motor1 = merek('Honda', 'Vario', 'Hitam', 125)
print(Motor1.Jenis)
print(Motor1.Nama)
print(Motor1.Warna)
print(Motor1.Kecepatan)

# E. Method
# contoh dejorator
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

# 1. Object Method
class Motor:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self): # menambahkan method 
        self.kecepatan += 10

Motor1 = Motor("Merah", "Honda", 150)
print("Sebelum ditambahkan: ")
print(Motor1.kecepatan)

Motor1.tambah_kecepatan() # memanggil method yang di tambahkan      

print("Setelah ditambahkan: ")
print(Motor1.kecepatan)

# 2. Static Method
class Motor:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_motor():
        print("Ini adalah metode dari kelas Motor")
        
Motor.intro_motor()
Motor1 = Motor("Honda")
Motor1.intro_motor()

# 3. Class Method
# > latihan 1
class Motor:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_motor(cls):
        print("Ini adalah metode dari kelas Motor")
        
Motor.intro_motor()
Motor1 = Motor("DicodingCar")
Motor1.intro_motor()

# > Latihan 2
class Motor:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_motor(*args):
        print(args)
        
Motor.intro_motor()
motorx = Motor("DicodingCar")
motorx.intro_motor()





