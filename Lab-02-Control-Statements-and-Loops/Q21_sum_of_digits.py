"""Lab solution: Sum of Digits
Question number: 21
"""

n = abs(int(input("Enter an integer: ")))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)
