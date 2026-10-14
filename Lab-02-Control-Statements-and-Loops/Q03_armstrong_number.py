"""Lab solution: Armstrong Number
Question number: 03
"""

n = input("Enter a non-negative integer: ")
if not n.isdigit():
    print("Enter a non-negative integer.")
else:
    power = len(n)
    total = sum(int(digit) ** power for digit in n)
    print("Armstrong number" if total == int(n) else "Not an Armstrong number")
