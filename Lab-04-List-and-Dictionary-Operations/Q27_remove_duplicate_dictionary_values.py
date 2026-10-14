"""Lab solution: Remove Duplicate Dictionary Values
Question number: 27
"""

data = {k: v for k, v in (input("Enter key value: ").split() for _ in range(int(input("Number of pairs: "))))}
result = {}
for key, value in data.items():
    if value not in result.values(): result[key] = value
print(result)
