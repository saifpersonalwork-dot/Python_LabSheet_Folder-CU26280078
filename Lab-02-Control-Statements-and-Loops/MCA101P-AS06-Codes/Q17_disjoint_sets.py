# Check whether two sets are disjoint
A = set(map(int, input("Enter integers for set A: ").split()))
B = set(map(int, input("Enter integers for set B: ").split()))
print("Sets are disjoint:", A.isdisjoint(B))
