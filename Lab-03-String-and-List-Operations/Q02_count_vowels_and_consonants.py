"""Lab solution: Count Vowels and Consonants
Question number: 02
"""

text = input("Enter a string: ")
vowels = consonants = 0
for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou": vowels += 1
        else: consonants += 1
print("Vowels:", vowels, "Consonants:", consonants)
