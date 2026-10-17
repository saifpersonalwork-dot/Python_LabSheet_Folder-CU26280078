# Check whether two strings are anagrams using sets
# Sets alone cannot account for repeated letter counts, so sorted characters are compared.
first = input("Enter the first string: ").replace(" ", "").lower()
second = input("Enter the second string: ").replace(" ", "").lower()
if sorted(first) == sorted(second):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
