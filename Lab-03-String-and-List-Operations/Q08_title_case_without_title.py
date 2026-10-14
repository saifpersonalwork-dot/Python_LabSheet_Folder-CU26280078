"""Lab solution: Title Case Without title()
Question number: 08
"""

text = input("Enter a string: ")
words = text.split()
result = []
for word in words:
    result.append(word[0].upper() + word[1:].lower() if word else word)
print(" ".join(result))
