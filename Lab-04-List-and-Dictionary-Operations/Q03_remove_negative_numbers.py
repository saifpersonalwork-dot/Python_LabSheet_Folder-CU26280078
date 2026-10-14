"""Lab solution: Remove Negative Numbers
Question number: 03
"""

numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
print([n for n in numbers if n >= 0])
