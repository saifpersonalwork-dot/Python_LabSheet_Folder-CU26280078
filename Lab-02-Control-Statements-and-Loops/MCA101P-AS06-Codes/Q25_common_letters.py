# Find common letters in two strings using sets
first = input("Enter the first string: ").lower()
second = input("Enter the second string: ").lower()
common = set(first) & set(second)
common.discard(" ")
print("Common letters:", common)
