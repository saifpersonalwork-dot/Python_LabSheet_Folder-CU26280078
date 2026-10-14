"""Lab solution: Common Elements in Two Lists
Question number: 28
"""

a = input("First list: ").split()
b = input("Second list: ").split()
common = []
for item in a:
    if item in b and item not in common: common.append(item)
print("Common elements:", common)
