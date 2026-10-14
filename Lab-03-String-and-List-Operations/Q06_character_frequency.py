"""Lab solution: Character Frequency
Question number: 06
"""

text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch, count in frequency.items():
    print(repr(ch), ":", count)
