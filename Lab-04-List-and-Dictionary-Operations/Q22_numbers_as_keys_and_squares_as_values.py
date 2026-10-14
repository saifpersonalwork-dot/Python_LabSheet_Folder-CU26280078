"""Lab solution: Numbers as Keys and Squares as Values
Question number: 22
"""

n = int(input("Enter n: "))
print({i: i * i for i in range(1, n + 1)})
