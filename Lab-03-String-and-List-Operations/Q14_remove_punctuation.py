"""Lab solution: Remove Punctuation
Question number: 14
"""

import string
text = input("Enter a string: ")
print("".join(ch for ch in text if ch not in string.punctuation))
