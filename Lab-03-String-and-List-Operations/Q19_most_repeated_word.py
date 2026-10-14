"""Lab solution: Most Repeated Word
Question number: 19
"""

import re
words = re.findall(r"\b\w+\b", input("Enter a sentence: ").lower())
if not words:
    print("No words entered.")
else:
    counts = {}
    for word in words: counts[word] = counts.get(word, 0) + 1
    best = max(counts, key=counts.get)
    print("Most repeated word:", best, "(count:", counts[best], ")")
