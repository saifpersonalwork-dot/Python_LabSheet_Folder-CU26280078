"""Lab solution: Palindrome Number
Question number: 02
"""

n = input("Enter a number: ")
print("Palindrome" if n == n[::-1] else "Not palindrome")
