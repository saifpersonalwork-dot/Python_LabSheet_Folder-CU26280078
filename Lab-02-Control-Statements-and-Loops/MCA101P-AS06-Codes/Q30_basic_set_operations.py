# Perform union, intersection, difference, and symmetric difference
A = set(map(int, input("Enter integers for set A: ").split()))
B = set(map(int, input("Enter integers for set B: ").split()))
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric difference:", A ^ B)
