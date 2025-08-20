# problem 13- Secure Login & Utility Program
import math

username = "admin"
password = "1234"

attempts = 0
while attempts < 3:
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == username and p == password:
        print("Login successful!\n")
        break
    else:
        print("Wrong credentials.")
        attempts += 1

if attempts == 3:
    print("Too many failed attempts. Exiting...")
    exit()

while True:
    print("\n--- Utility Program ---")
    print("1. Number System Converter")
    print("2. Bitwise Operations")
    print("3. Trigonometry Calculator")
    print("4. Grade Calculator")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        num = int(input("Enter decimal number: "))
        print("Binary:", bin(num))
        print("Octal:", oct(num))
        print("Hexadecimal:", hex(num))

    elif choice == "2":
        a = int(input("Enter first int: "))
        b = int(input("Enter second int: "))
        print("AND:", a & b)
        print("OR:", a | b)
        print("XOR:", a ^ b)
        print("NOT a:", (~a) & 255)
        print("NOT b:", (~b) & 255)

    elif choice == "3":
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)
        print("sin:", math.sin(rad))
        print("cos:", math.cos(rad))
        print("tan:", math.tan(rad))

    elif choice == "4":
        marks = int(input("Enter marks (0–100): "))
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "Fail"
        print("Grade:", grade)
        print("Marks are", "Even" if marks & 1 == 0 else "Odd")

    elif choice == "5":
        print("Thanks for using...Goodbye!")
        break

    else:
        print("Invalid choice.")
