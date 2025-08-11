# problem_07.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Cannot divide by zero")
print("Power:", a ** b)
print("a > b:", a > b)
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Even/Odd check:", "Even" if a & 1 == 0 else "Odd")
