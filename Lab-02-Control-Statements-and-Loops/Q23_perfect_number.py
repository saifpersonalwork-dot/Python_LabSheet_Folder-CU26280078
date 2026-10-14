"""Lab solution: Perfect Number
Question number: 23
"""

n = int(input("Enter a positive integer: "))
total = 0
for d in range(1, n):
    if d > 0 and n % d == 0:
        total += d
print("Perfect number" if n > 0 and total == n else "Not a perfect number")
