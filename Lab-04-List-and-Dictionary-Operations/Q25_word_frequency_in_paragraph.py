"""Lab solution: Word Frequency in Paragraph
Question number: 25
"""

import re
words = re.findall(r"\b\w+\b", input("Enter a paragraph: ").lower())
frequency = {}
for word in words: frequency[word] = frequency.get(word, 0) + 1
print(frequency)
