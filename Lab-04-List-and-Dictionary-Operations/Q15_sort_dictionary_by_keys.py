"""Lab solution: Sort Dictionary by Keys
Question number: 15
"""

data = {k: v for k, v in (input("Enter key value pair: ").split(maxsplit=1) for _ in range(int(input("Number of pairs: "))))}
print(dict(sorted(data.items())))
