"""Lab solution: String Rotation Check
Question number: 20
"""

a = input("First string: ")
b = input("Second string: ")
print("Rotations" if len(a) == len(b) and b in (a + a) else "Not rotations")
