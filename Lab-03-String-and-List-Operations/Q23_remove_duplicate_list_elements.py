"""Lab solution: Remove Duplicate List Elements
Question number: 23
"""

numbers = input("Enter items separated by spaces: ").split()
unique = []
for item in numbers:
    if item not in unique: unique.append(item)
print(unique)
