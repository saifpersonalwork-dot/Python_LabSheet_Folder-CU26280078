"""Lab solution: Prime Number Check
Question number: 30
"""

n = int(input("Enter an integer: "))
if n < 2:
    print("Not prime")
else:
    prime = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            prime = False
            break
        divisor += 1
    print("Prime" if prime else "Not prime")
