import random
pas = int(input("Masukan Panjang Digit:"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pasword = "".join(random.sample(s,pas ))
print(pasword)