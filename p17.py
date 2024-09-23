air = str(input("Masukan Kondisi Air: "))
if air == "mendidih":
    print("MATIIN WOI!!")
else:
    print("input salah")

suhu = int(input("masukan suhu ruangan: "))
if suhu > 45:
    print("PANAS SETANGG!")
elif suhu < 20:
    print("Dingin,Tetapi Tidak Kejam")
else:
    print("Haneut Bos")
    

mobil = input("Masukan Kondisi Mobil: ")
if mobil == 'rusak':
    print("naik motor bos")
elif mobil == 'bagus':
    print("lembergember")
else:
    print("input salah")

angka = int(input("Masukan Angka:"))
if angka % 2 == 0:
    print("Ini Angka Genap")
elif angka % 2 != 0:
    print("Ini Angka Ganjil")
else :
    print('idiot')
    

adit = input("Kumaha Si Adit Teh: ")
if adit == 'dongo':
    print('sotoy maneh')
elif adit == 'pinter':
    print("PEMBOHONK PUBLIK!!")
else: 
    print("awokwokaokwok")