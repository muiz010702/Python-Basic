"""
Diberikan bilangan bulat, , lakukan tindakan bersyarat berikut:

Jika ganjil, cetak Aneh
Jika genap dan dalam rentang inklusif 2 hingga 5 , cetak Tidak Aneh
Jika genap dan dalam kisaran inklusif 6 hingga 20 , cetak Aneh
Jika genap dan lebih besar dari 20, cetak Tidak Aneh
"""
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 3 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    
