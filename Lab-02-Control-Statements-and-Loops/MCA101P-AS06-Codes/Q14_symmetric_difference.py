# Find the symmetric difference of two sets
A = set(map(int, input("Enter integers for set A, separated by spaces: ").split()))
B = set(map(int, input("Enter integers for set B, separated by spaces: ").split()))
print("Symmetric difference:", A ^ B)
