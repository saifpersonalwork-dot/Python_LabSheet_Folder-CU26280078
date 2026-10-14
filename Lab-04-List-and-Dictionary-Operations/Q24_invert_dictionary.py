"""Lab solution: Invert Dictionary
Question number: 24
"""

data = {k: v for k, v in (input("Enter key value: ").split() for _ in range(int(input("Number of pairs: "))))}
inverted = {value: key for key, value in data.items()}
print(inverted)
