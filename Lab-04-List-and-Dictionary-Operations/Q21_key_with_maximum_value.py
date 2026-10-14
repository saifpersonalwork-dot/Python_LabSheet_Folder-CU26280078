"""Lab solution: Key with Maximum Value
Question number: 21
"""

data = {k: float(v) for k, v in (input("Enter key numeric_value: ").split() for _ in range(int(input("Number of pairs: "))))}
if data: print("Key with maximum value:", max(data, key=data.get))
else: print("Dictionary is empty")
