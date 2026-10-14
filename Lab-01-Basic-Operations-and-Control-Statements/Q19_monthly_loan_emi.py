"""Lab solution: Monthly Loan EMI
Question number: 19
"""

principal = float(input("Loan amount: "))
annual_rate = float(input("Annual interest rate (%): "))
months = int(input("Loan term (months): "))
if months <= 0 or principal < 0 or annual_rate < 0:
    print("Enter valid non-negative values and a positive term.")
else:
    r = annual_rate / 1200
    emi = principal / months if r == 0 else principal * r * (1 + r) ** months / ((1 + r) ** months - 1)
    print("Monthly EMI:", round(emi, 2))
