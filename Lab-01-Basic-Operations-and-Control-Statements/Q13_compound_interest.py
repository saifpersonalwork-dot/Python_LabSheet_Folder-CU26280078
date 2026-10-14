"""Lab solution: Compound Interest
Question number: 13
"""

principal = float(input("Principal: "))
rate = float(input("Annual rate (%): "))
time = float(input("Time (years): "))
amount = principal * (1 + rate / 100) ** time
print("Amount:", round(amount, 2))
print("Compound interest:", round(amount - principal, 2))
