"""Lab solution: HCF Using Loop
Question number: 28
"""

a = abs(int(input("First integer: ")))
b = abs(int(input("Second integer: ")))
hcf = 1
for d in range(1, min(a, b) + 1):
    if a % d == 0 and b % d == 0:
        hcf = d
print("HCF:", hcf if a or b else 0)
