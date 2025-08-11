# problem_04.py
salaries = {
    "Sumaiya": 20000,
    "Ahmed": 30000,
    "Pew": 25000,
    "Rew": 40000
}

yearly_data = [(name, sal * 12) for name, sal in salaries.items()]
highest = max(yearly_data, key=lambda x: x[1])
avg_salary = sum(s for _, s in yearly_data) / len(yearly_data)
above_avg = [n for n, s in yearly_data if s > avg_salary]

print("Highest salary:", highest)
print("Average yearly salary:", avg_salary)
print("Above average:", above_avg)
