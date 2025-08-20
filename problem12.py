# problem 12 Student Report Card Generator
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = []

for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
avg = total / len(marks)

if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else:
    grade = "Fail"

roll_type = "Even" if roll & 1 == 0 else "Odd"

print("\n--- Report Options ---")
print("1. Normal")
print("2. Encoded")
choice = input("Enter choice: ")

if choice == "1":
    print("\n--- Report Card ---")
    print("Name:", name)
    print("Roll:", roll, f"({roll_type})")
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)

elif choice == "2":
    print("\n--- Encoded Report ---")
    print("Name:", name)
    print("Roll (binary):", bin(roll))
    print("Total:", total)
    print("Average:", avg)
    print("Grade (ASCII code):", [ord(c) for c in grade])

print("\n--- Swap Roll and Average ---")
print("Before:", "Roll =", roll, "Avg =", avg)
roll, avg = avg, roll
print("After:", "Roll =", roll, "Avg =", avg)
