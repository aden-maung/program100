import random

n = random.randrange(1,10)

guess = int(input("Tebak Angka: "))
while n!= guess: 
    
    if guess < n:
        print("aden kayak kontol")
        
        guess = int(input("Masukin Nomor Lagi: "))
    
    elif guess > n:
        print("aden cabul tingkat dewa")
        
        guess = int(input("Masukin Nomor Lagi: "))
    
    else:
        break
print("GELOOO BENER CUYY!!")
print('Makasih Sudah Mencoba:)')