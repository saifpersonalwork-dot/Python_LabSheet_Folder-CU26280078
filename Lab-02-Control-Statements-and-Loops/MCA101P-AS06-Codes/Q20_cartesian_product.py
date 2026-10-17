# Find the Cartesian product of two sets
A = set(input("Enter items for set A separated by spaces: ").split())
B = set(input("Enter items for set B separated by spaces: ").split())
product = {(a, b) for a in A for b in B}
print("Cartesian product:", product)
