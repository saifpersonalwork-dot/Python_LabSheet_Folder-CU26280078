"""Lab solution: Sum and Average of List
Question number: 01
"""

numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
if numbers: print("Sum:", sum(numbers), "Average:", sum(numbers) / len(numbers))
else: print("List is empty")
