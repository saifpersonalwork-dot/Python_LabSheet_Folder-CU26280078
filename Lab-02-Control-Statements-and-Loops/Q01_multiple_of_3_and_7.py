"""Lab solution: Multiple of 3 and 7
Question number: 01
"""

n = int(input("Enter an integer: "))
print("Multiple of both 3 and 7" if n % 3 == 0 and n % 7 == 0 else "Not a multiple of both")
