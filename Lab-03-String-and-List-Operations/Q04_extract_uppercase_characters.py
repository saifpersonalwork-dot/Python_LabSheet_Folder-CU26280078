"""Lab solution: Extract Uppercase Characters
Question number: 04
"""

text = input("Enter a string: ")
print("".join(ch for ch in text if ch.isupper()))
