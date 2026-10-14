"""Lab solution: Quotient and Remainder
Question number: 04
"""

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Division by zero is not allowed.")
else:
    print("Quotient:", a // b)
    print("Remainder:", a % b)
