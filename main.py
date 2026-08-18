import math

print("=== Calculator ===")

def operations_menu():
    while True:
        print ("Select an option: ")
        print("1. Addition 2. Subtraction 3. Multiplication 4. Division")
        option = input("5. Radiciation 6. Exponential 7. Logarhytm  8. Base Numbers 9. Exit: ").strip().lower()
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
            log_menu()
        elif option in ("9", "back", "exit", "return"):
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
        add_option = input("Another addition? [Y/N]: ").strip().lower()
        if add_option in ("n", "no"):
            return

def subtraction(a, b):
    return a - b

def subtraction_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = subtraction(first_number, second_number)
        print(result)
        subtract_option = input("Another subtraction? [Y/N]: ").strip().lower()
        if subtract_option in ("n", "no"):
            return

def multiplication(a, b):
    return a * b

def multiplication_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = multiplication(first_number, second_number)
        print(result)
        multiply_option = input("Another multiplication? [Y/N]: ").strip().lower()
        if multiply_option in ("n", "no"):
            return

def division(a, b):
    return a / b

def division_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number: "))
        result = division(first_number, second_number)
        print(result)
        divide_option = input("Another division? [Y/N]: ").strip().lower()
        if divide_option in ("n", "no"):
            return

def power(a, b):
    return a ** b

def power_menu():
    while True:
        first_number = float(input("Base: "))
        second_number = float(input("Exponent: "))
        result = power(first_number, second_number)
        print(result)
        power_option = input("Another power? [Y/N]: ").strip().lower()
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
        root_option = input("Another root? [Y/N]: ").strip().lower()
        if root_option in ("n", "no"):
            return

def log(a, b):
    return 

def log_menu():
    while True:
        first_number = float(input("First Number: "))
        second_number = float(input("Second Number"))
        third_number = float(input("Third Number: "))
        result = log(first_number, second_number, third_number)
        print(result)
        log_option = input("Another Log? [Y/N]: ").strip().lower()
        if log_option in ("n", "no"):
            return

if __name__ == "__main__":
    operations_menu()