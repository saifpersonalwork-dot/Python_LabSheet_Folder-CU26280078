"""Lab solution: Multiplication Tables 1 to 10
Question number: 27
"""

for n in range(1, 11):
    print(f"Table of {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()
