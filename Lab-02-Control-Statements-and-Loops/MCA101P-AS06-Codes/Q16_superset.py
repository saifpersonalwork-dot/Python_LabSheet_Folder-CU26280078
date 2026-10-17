# Check if one set is a superset of another
A = set(map(int, input("Enter integers for set A: ").split()))
B = set(map(int, input("Enter integers for set B: ").split()))
print("A is a superset of B:", A.issuperset(B))
