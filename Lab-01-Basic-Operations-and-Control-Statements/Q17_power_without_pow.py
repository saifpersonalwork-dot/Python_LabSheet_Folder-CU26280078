"""Lab solution: Power Without pow()
Question number: 17
"""

base = float(input("Base: "))
exponent = int(input("Non-negative integer exponent: "))
if exponent < 0:
    print("Please enter a non-negative exponent.")
else:
    result = 1
    for _ in range(exponent):
        result *= base
    print("Result:", result)
