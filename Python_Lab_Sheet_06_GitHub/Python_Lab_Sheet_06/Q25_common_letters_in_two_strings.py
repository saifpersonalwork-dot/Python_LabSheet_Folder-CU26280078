# Q25: Find common letters in two strings using sets
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")
common = set(text1.lower()) & set(text2.lower())
common.discard(" ")
print("Common letters:", common)
