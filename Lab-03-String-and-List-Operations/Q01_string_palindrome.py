"""Lab solution: String Palindrome
Question number: 01
"""

text = input("Enter a string: ")
clean = "".join(ch.lower() for ch in text if ch.isalnum())
print("Palindrome" if clean == clean[::-1] else "Not palindrome")
