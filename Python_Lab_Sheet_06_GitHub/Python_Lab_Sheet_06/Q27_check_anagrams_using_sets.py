# Q27: Check if two strings are anagrams using sets
text1 = input("Enter first string: ").replace(" ", "").lower()
text2 = input("Enter second string: ").replace(" ", "").lower()

# Compare character sets and frequency of each character.
same_characters = set(text1) == set(text2)
same_counts = all(text1.count(ch) == text2.count(ch) for ch in set(text1) | set(text2))

if same_characters and same_counts and len(text1) == len(text2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
