"""Lab solution: Check Dictionary Key
Question number: 19
"""

data = {"name": "Aman", "marks": 75}
key = input("Enter key to search: ")
print("Key exists" if key in data else "Key does not exist")
