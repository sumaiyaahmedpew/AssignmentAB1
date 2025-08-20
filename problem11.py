# problem 11 - Scientific Calculator with Modes
import math

def basic_mode():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    swap_choice = input("Do you want to swap numbers? (y/n): ")
    if swap_choice.lower() == "y":
        a, b = b, a
        print("Numbers swapped: a =", a, "b =", b)

    op = input("Enter operator (+,-,*,/,//,%,**): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b if b != 0 else "Division by zero!")
    elif op == "//":
        print("Result:", a // b if b != 0 else "Division by zero!")
    elif op == "%":
        print("Result:", a % b if b != 0 else "Division by zero!")
    elif op == "**":
        print("Result:", a ** b)
    else:
        print("Invalid operator")


def advanced_mode():
    while True:
        print("\n--- Advanced Mode ---")
        print("1. Number System Conversion")
        print("2. Bitwise Calculator")
        print("3. Geometry Calculator")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            num = int(input("Enter decimal number: "))
            print("Binary:", bin(num))
            print("Octal:", oct(num))
            print("Hexadecimal:", hex(num))

            n, binary = num, ""
            while n > 0:
                binary = str(n % 2) + binary
                n //= 2
            print("Manual Binary:", binary)

            binary_input = input("Enter binary to convert to decimal: ")
            print("Decimal:", int(binary_input, 2))

        elif choice == "2":
            a = int(input("Enter first int: "))
            b = int(input("Enter second int: "))
            print("AND:", a & b)
            print("OR:", a | b)
            print("XOR:", a ^ b)
            print("NOT a:", (~a) & 255)
            print("NOT b:", (~b) & 255)

        elif choice == "3":
            r = float(input("Enter radius: "))
            area = math.pi * r * r
            circum = 2 * math.pi * r
            print("Area:", area)
            print("Circumference:", circum)
            print("Sqrt(area):", math.sqrt(area))

            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("sin:", math.sin(rad))
            print("cos:", math.cos(rad))
            print("tan:", math.tan(rad))

        elif choice == "4":
            break
        else:
            print("Invalid choice")


while True:
    print("\n--- Scientific Calculator ---")
    print("1. Basic Mode")
    print("2. Advanced Mode")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        basic_mode()
    elif choice == "2":
        advanced_mode()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
