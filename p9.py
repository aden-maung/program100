print("="*40)
print("PROGRAM TABUNG")
print("="*40)

r = float(input("masukan jari jari: "))
t = float(input("masukan tinggi: "))

v = 3.14 * r * r * t
lp = (2 * 3.14 * r * t) + (2 * (2 * 3.14 * r))

print("VOLUME: ",v, " cm3")
print("Luas Permukaan: ",lp, " cm2")