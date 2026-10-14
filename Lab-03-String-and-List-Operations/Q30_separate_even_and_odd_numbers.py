"""Lab solution: Separate Even and Odd Numbers
Question number: 30
"""

numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]
print("Even:", even)
print("Odd:", odd)
