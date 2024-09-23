def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Pilih:")
    print("+")
    print("-")
    print("X")
    print("/")

    choice = input("Pilih Sok (+|-|X|/ ): ")

    if choice in ['+', '-', 'X', '/']:
        num1 = float(input("Nomor Pertama: "))
        num2 = float(input("Nomor Kedua: "))

        if choice == '+':
            print(f"=: {add(num1, num2)}")

        elif choice == '-':
            print(f"=: {subtract(num1, num2)}")

        elif choice == 'X':
            print(f"=: {multiply(num1, num2)}")

        elif choice == '/':
            print(f"=: {divide(num1, num2)}")

    else:
        print("Invalid")

calculator()

