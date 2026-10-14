"""Lab solution: Uppercase Lowercase or Digit
Question number: 28
"""

ch = input("Enter one character: ")
if len(ch) != 1:
    print("Enter exactly one character.")
elif ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Other character")
