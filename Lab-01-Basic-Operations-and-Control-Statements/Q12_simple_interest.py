"""Lab solution: Simple Interest
Question number: 12
"""

principal = float(input("Principal: "))
rate = float(input("Annual rate (%): "))
time = float(input("Time (years): "))
print("Simple interest:", principal * rate * time / 100)
