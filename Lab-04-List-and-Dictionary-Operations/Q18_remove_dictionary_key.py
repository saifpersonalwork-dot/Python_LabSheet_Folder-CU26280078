"""Lab solution: Remove Dictionary Key
Question number: 18
"""

data = {"name": "Aman", "marks": 75, "city": "Meerut"}
key = input("Key to remove (name/marks/city): ")
if key in data: del data[key]
else: print("Key not found")
print(data)
