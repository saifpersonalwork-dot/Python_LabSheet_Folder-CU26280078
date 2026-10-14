"""Lab solution: Sum Dictionary Values
Question number: 20
"""

data = {k: float(v) for k, v in (input("Enter key value: ").split() for _ in range(int(input("Number of pairs: "))))}
print("Sum of values:", sum(data.values()))
