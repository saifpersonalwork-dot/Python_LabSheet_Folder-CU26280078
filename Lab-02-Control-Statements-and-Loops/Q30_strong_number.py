"""Lab solution: Strong Number
Question number: 30
"""

n = int(input("Enter a non-negative integer: "))
def factorial(value):
    result = 1
    for i in range(2, value + 1):
        result *= i
    return result
total = sum(factorial(int(digit)) for digit in str(n)) if n >= 0 else -1
print("Strong number" if total == n else "Not a strong number")
