"""Lab solution: First Non-Repeated Character
Question number: 15
"""

text = input("Enter a string: ")
for ch in text:
    if text.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character")
