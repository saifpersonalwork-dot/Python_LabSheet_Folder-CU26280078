"""Lab solution: Common Dictionary Keys
Question number: 29
"""

first = dict.fromkeys(input("First dictionary keys: ").split())
second = dict.fromkeys(input("Second dictionary keys: ").split())
print("Common keys:", list(first.keys() & second.keys()))
