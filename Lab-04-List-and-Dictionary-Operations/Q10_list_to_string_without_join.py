"""Lab solution: List to String Without join
Question number: 10
"""

items = input("Enter items separated by spaces: ").split()
result = ""
for item in items:
    if result: result += " "
    result += item
print(result)
