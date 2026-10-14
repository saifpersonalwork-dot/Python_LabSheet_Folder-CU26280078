"""Lab solution: All Substrings
Question number: 17
"""

text = input("Enter a string: ")
for start in range(len(text)):
    for end in range(start + 1, len(text) + 1):
        print(text[start:end])
