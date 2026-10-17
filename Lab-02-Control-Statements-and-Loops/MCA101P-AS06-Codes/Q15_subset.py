# Check if one set is a subset of another
A = set(map(int, input("Enter integers for set A: ").split()))
B = set(map(int, input("Enter integers for set B: ").split()))
print("A is a subset of B:", A.issubset(B))
