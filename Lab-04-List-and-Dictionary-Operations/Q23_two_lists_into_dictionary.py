"""Lab solution: Two Lists into Dictionary
Question number: 23
"""

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()
if len(keys) != len(values): print("Lists must have the same length")
else: print(dict(zip(keys, values)))
