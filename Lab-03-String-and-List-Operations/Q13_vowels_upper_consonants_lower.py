"""Lab solution: Vowels Upper Consonants Lower
Question number: 13
"""

text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.lower() in "aeiou": result += ch.upper()
    elif ch.isalpha(): result += ch.lower()
    else: result += ch
print(result)
