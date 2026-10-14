"""Lab solution: Number in a Range
Question number: 29
"""

n = float(input("Number: "))
low = float(input("Range start: "))
high = float(input("Range end: "))
if low > high:
    low, high = high, low
print("Inside range" if low <= n <= high else "Outside range")
