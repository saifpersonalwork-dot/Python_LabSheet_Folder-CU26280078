"""Lab solution: Reverse String Without Slicing
Question number: 07
"""

text = input("Enter a string: ")
result = ""
for ch in text:
    result = ch + result
print(result)
