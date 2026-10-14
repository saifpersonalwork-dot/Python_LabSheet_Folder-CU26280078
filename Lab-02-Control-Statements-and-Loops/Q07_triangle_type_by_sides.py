"""Lab solution: Triangle Type by Sides
Question number: 07
"""

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")
