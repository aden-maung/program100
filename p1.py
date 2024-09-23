T = 365
B = 30
h = int(input("masukan hari: "))
t = int(h / T)
h = h % T
b = int(h / B)
h = h % B

print(t, ' tahun',b, ' bulan ', ' dan ',h,' hari ')