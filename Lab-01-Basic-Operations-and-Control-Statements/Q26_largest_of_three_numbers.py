"""Lab solution: Largest of Three Numbers
Question number: 26
"""

a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest:", largest)
