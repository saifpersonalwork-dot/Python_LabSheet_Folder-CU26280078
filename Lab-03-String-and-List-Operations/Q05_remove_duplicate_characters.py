"""Lab solution: Remove Duplicate Characters
Question number: 05
"""

text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in result:
        result += ch
print(result)
