"""Lab solution: Difference Between Two Lists
Question number: 29
"""

a = input("First list: ").split()
b = input("Second list: ").split()
print("Items in first but not second:", [item for item in a if item not in b])
