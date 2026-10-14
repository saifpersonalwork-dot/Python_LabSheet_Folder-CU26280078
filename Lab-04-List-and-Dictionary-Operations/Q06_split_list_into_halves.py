"""Lab solution: Split List into Halves
Question number: 06
"""

items = input("Enter items separated by spaces: ").split()
mid = (len(items) + 1) // 2
print("First half:", items[:mid])
print("Second half:", items[mid:])
