Number = [1,2,3,4,5]
Number.append(8)
print(Number)
# tipe data array menggunakan library python
import array

M = array.array = ("M",[1,2,1,2,1,4])
print(M)
print(type(M))
# membuat array dengan list serta mengecek lokasi penyimpanan yg berbeda
var_list = [1,2,3,4]
for elemen in var_list:
    print(id(elemen))

# membuat array dengan list
Nilai = [50,60,70,80,90,100]
print(Nilai)

# membuat array dengan mendefinisikan nilai default
huruf = [0 for A in range(15)]
print(huruf)

K = [0 for A in range(15)]

for A in range(15):
    K[A] = A
print(K)

# pemrosesan sekuensial pada array
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")
