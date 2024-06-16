#belajar membuat program sederhana list dan range menggunakan for loop

Data = int(input("Data mobil yang tersedia: "))

mobil = []
tahun = []

for M in range(0, Data):
    print(f"Data ke {M}")
    input_mobil = input("Nama = ")
    input_tahun = int(input("tahun keluaran = "))

    mobil.append(input_mobil)
    tahun.append(input_tahun)
    
for M in range(0, len(mobil)):
    Data_Mobil = mobil[M]
    Data_Tahun = tahun[M]
    print(f"Mobil {Data_Mobil} tahun keluaran {Data_Tahun}")
