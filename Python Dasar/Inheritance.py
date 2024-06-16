# Inheritance atau pewarisan
# sebelum ada pewarisan
class Motor:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

Motorx = Motor("biru", "honda", 125)
print(Motorx.merek)
# sesudah ada pewarisan
class Motor:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MotorSport(Motor):
    def turbo(self):
        self.kecepatan += 50

# Kelas Motor Dasar
Motorx = Motor("Merah", "Honda", 125)
print(Motorx.kecepatan)

# Kelas Motor Sport
motor_sport_1 = MotorSport("Hitam", "kawaski", 160)
print(motor_sport_1.kecepatan)
motor_sport_1.turbo()
print(motor_sport_1.kecepatan)

# OVERRIDE
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "Honda", 200)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

# SUPER
class Motor:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MotorSport(Motor):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
motor_sport_1 = MotorSport("Hitam", "Honda", 180)
motor_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(motor_sport_1.kecepatan)


