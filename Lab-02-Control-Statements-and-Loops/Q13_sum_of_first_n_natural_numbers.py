"""Lab solution: Sum of First N Natural Numbers
Question number: 13
"""

n = int(input("Enter n: "))
if n < 0:
    print("Enter a non-negative integer.")
else:
    total = 0
    for number in range(1, n + 1):
        total += number
    print("Sum:", total)
