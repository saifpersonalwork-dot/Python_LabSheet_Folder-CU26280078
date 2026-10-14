"""Lab solution: Rotate List by N Positions
Question number: 02
"""

items = input("Enter items separated by spaces: ").split()
n = int(input("Rotate right by how many positions? "))
if items:
    n %= len(items)
    items = items[-n:] + items[:-n] if n else items
print(items)
