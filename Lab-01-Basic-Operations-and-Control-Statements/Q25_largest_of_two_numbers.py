"""Lab solution: Largest of Two Numbers
Question number: 25
"""

a = float(input("First number: "))
b = float(input("Second number: "))
if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both numbers are equal")
