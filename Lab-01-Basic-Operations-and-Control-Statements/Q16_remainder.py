"""Lab solution: Remainder
Question number: 16
"""

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Division by zero is not allowed.")
else:
    print("Remainder:", a % b)
