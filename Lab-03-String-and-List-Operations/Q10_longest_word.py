"""Lab solution: Longest Word
Question number: 10
"""

words = input("Enter a sentence: ").split()
if not words:
    print("No words entered.")
else:
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest): longest = word
    print("Longest word:", longest)
