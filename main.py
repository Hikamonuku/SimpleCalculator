import math

print("=== Calculator ===")

def operations_menu():
    while True:
        print ("Select an option: ")
        print("1. Addition 2. Subtraction 3. Multiplication 4. Division")
        option = input("5. Radiciation 6. Exponential 7. Logarhytm  8. Base Numbers 9. Back: ").strip().lower()
        if option in ("1", "addition", "add"):
            addition_menu()
        elif option in ("2", "subtraction", "subtract"):
            subtraction_menu()
        elif option in ("3", "multiplication", "multiply"):
            multiplication_menu()
        elif option in ("4", "division"):
            division_menu()
        elif option in ("5", "root", "radiciation"):
            root_menu()
        elif option in ("6", "exponential", "power"):
            power_menu()
        elif option in ("7", "log"):
            pass
        elif option in ("9", "back", "exit"):
            break
        else:
            print("Invalid option. ")

def addition(a, b):
    return a + b

def addition_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = addition(first_number, second_number)
        print(result)
        add_option = input("Another addition? [Y/N]: ")
        if add_option in ("N", "no"):
            return

def subtraction(a, b):
    return a - b

def subtraction_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = subtraction(first_number, second_number)
        print(result)
        subtract_option = input("Another subtraction? [Y/N]: ")
        if subtract_option in ("N", "no"):
            return

def multiplication(a, b):
    return a * b

def multiplication_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = multiplication(first_number, second_number)
        print(result)
        multiply_option = input("Another multiplication? [Y/N]: ")
        if multiply_option in ("N", "no"):
            return

def division(a, b):
    return a / b

def division_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = division(first_number, second_number)
        print(result)
        divide_option = input("Another division? [Y/N]: ")
        if divide_option in ("N", "no"):
            return

def power(a, b):
    return a ** b

def power_menu():
    while True:
        first_number = float(input("Base: "))
        second_number = float(input("Exponent: "))
        result = power(first_number, second_number)
        print(result)
        power_option = input("Another power? [Y/N]: ")
        if power_option in ("n", "no"):
            return

def root(base, index):
    return power(base, 1/index)

def root_menu():
    while True:
        first_number = float(input("Radicand: "))
        second_number = float(input("Index: "))
        result = root(first_number, second_number)
        print(result)
        root_option = input("Another root? [Y/N]: ")
        if root_option in ("n", "no"):
            return

if __name__ == "__main__":
    operations_menu()