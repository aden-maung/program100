import random

print ("="*40)
print ("COIN FLIP")
print ("="*40)

h = random . randint (1,2)
coin = str(input("Heads or Tails:"))
he = ("HEADS")
t = ("TAILS")

if coin == he and h == 1:
    print ("ITS HEADS")
elif coin == t and h == 2:
    print ("ITS TAILS")
elif coin == he and h != 1:
    print("ITS TAILS")
elif coin == t and h != 2:
    print("ITS HEADS")
else:
    print("de fak bro")
