"""Lab solution: Update Dictionary Value
Question number: 17
"""

data = {"name": "Aman", "marks": 75}
key = input("Key to update (name/marks): ")
if key in data:
    data[key] = input("New value: ")
    print(data)
else: print("Key not found")
