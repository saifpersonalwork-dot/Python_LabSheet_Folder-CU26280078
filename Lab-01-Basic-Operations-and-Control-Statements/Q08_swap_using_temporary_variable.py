"""Lab solution: Swap Using Temporary Variable
Question number: 08
"""

a = input("Enter a: ")
b = input("Enter b: ")
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)
