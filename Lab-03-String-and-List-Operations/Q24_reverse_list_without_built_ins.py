"""Lab solution: Reverse List Without Built-ins
Question number: 24
"""

items = input("Enter items separated by spaces: ").split()
left, right = 0, len(items) - 1
while left < right:
    items[left], items[right] = items[right], items[left]
    left += 1; right -= 1
print(items)
