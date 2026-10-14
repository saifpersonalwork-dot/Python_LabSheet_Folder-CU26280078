"""Lab solution: List Element Frequency
Question number: 25
"""

items = input("Enter items separated by spaces: ").split()
frequency = {}
for item in items: frequency[item] = frequency.get(item, 0) + 1
print(frequency)
