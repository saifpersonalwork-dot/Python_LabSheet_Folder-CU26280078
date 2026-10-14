"""Lab solution: Second Largest Distinct Number
Question number: 27
"""

numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
unique = sorted(set(numbers))
if len(unique) < 2: print("Need at least two distinct numbers")
else: print("Second largest:", unique[-2])
