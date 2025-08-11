# problem_08.py

items = [1, "apple", 3.5, "banana", True, 42, "cherry", 2.7, 1]

ints = list({x for x in items if type(x) == int})
floats = list({x for x in items if type(x) == float})
strings = list({x for x in items if type(x) == str})
bools = list({x for x in items if type(x) == bool})

print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", bools)
print("Counts:", {
    "int": len(ints),
    "float": len(floats),
    "string": len(strings),
    "bool": len(bools)
})
