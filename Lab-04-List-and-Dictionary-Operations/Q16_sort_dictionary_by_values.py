"""Lab solution: Sort Dictionary by Values
Question number: 16
"""

data = {k: float(v) for k, v in (input("Enter key numeric_value: ").split() for _ in range(int(input("Number of pairs: "))))}
print(dict(sorted(data.items(), key=lambda item: item[1])))
