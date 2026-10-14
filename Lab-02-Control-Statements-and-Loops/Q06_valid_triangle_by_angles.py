"""Lab solution: Valid Triangle by Angles
Question number: 06
"""

a = float(input("First angle: "))
b = float(input("Second angle: "))
c = float(input("Third angle: "))
print("Valid triangle" if a > 0 and b > 0 and c > 0 and a + b + c == 180 else "Invalid triangle")
