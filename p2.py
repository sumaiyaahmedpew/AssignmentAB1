# problem_02.py

data = [
    ("Sumaiya", 101, [80, 75, 90]),
    ("Ahmed", 102, [60, 70, 65]),
    ("Pew", 103, [90, 95, 92]),
    ("Rew", 104, [55, 48, 60])
]

students = {}

# Process each student's data
for name, roll, marks in data:
    total = sum(marks)
    avg = total // len(marks)

    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "avg": avg,
        "grade": grade
    }

# Helper function to get total marks for sorting
def get_total(student_item):
    return student_item[1]["total"]

# Top 3 students by total marks
top3 = sorted(students.items(), key=get_total, reverse=True)[:3]
print("Top 3 students:", top3)

# Failed students
fails = [v for v in students.values() if v["grade"] == "F"]
print("Failed students:", fails)
