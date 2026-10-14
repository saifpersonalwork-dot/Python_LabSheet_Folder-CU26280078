"""Lab solution: Sort List Ascending and Descending
Question number: 22
"""

numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
