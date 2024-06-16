class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    # Method deskripsi
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    # Method suara
    def suara(self):
        return "meow!"

# Membuat instance dari kelas Cat
myCat = Cat(name="Neko", age=3, species="Persian")

# menampilkan outputnya
print(myCat.deskripsi())
print(myCat.suara())      
