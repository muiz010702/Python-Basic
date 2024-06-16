Mobil= []

def Print_Data():
    print("===============")
    for Data in Mobil:
        print(Data)

Mobil.append ("Honda HRV")
Print_Data()

Mobil.append ("Honda Yaris")
Print_Data()

Mobil.append ("KIA Seltos")
Print_Data()

Mobil.append ("Mazda CX5")
Print_Data()

def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

pay_fulltime = get_pay(40)
print(pay_fulltime)

