"""Lab solution: Merge Two Dictionaries
Question number: 14
"""

first = {k: int(v) for k, v in (input("First dictionary pair key value: ").split() for _ in range(int(input("Number of pairs in first dictionary: "))))}
second = {k: int(v) for k, v in (input("Second dictionary pair key value: ").split() for _ in range(int(input("Number of pairs in second dictionary: "))))}
print({**first, **second})
