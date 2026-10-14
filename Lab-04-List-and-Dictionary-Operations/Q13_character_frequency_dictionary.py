"""Lab solution: Character Frequency Dictionary
Question number: 13
"""

text = input("Enter a string: ")
frequency = {}
for ch in text: frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)
