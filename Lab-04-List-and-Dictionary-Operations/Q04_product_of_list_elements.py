"""Lab solution: Product of List Elements
Question number: 04
"""

numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
product = 1
for n in numbers: product *= n
print("Product:", product)
