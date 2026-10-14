"""Lab solution: Fibonacci Series
Question number: 18
"""

n = int(input("Number of terms: "))
a, b = 0, 1
if n <= 0:
    print("Enter a positive number of terms.")
else:
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
