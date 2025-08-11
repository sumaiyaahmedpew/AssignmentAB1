# problem_05.py
followers_A = {"Rakhi", "Ramisa", "Sumaiya", "Liza"}
followers_B = {"Ramisa", "Sumaiya", "Jui"}

print("Common followers:", followers_A & followers_B)
print("Unique to A:", followers_A - followers_B)
print("Unique to B:", followers_B - followers_A)
print("All followers:", followers_A | followers_B)
