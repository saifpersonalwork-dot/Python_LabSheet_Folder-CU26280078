"""Lab solution: Vowel or Consonant
Question number: 27
"""

ch = input("Enter one alphabet character: ").lower()
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character.")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
