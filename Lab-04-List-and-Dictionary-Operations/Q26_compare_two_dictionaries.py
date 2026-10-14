"""Lab solution: Compare Two Dictionaries
Question number: 26
"""

first = {k: v for k, v in (input("First dictionary key value: ").split() for _ in range(int(input("Pairs in first dictionary: "))))}
second = {k: v for k, v in (input("Second dictionary key value: ").split() for _ in range(int(input("Pairs in second dictionary: "))))}
print("Dictionaries are equal" if first == second else "Dictionaries are not equal")
