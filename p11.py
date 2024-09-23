USERNAME = 'aden'
PASWORD = '12345678'

input_username = input('masukan username: ')
input_pasword = input('masukan pasword: ')
if USERNAME == input_username and PASWORD == input_pasword:
    print ("Welcome To Mobile Legend")

elif USERNAME == input_username and PASWORD != input_pasword:
    print("pasword na salah")

elif USERNAME != input_username and PASWORD == input_pasword:
    print("username tidak tersedia")

else:
    print ("salah goblok")
 