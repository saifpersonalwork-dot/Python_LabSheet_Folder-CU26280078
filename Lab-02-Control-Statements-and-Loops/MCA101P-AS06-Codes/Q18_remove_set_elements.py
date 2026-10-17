# Remove all elements of set B from set A
A = set(map(int, input("Enter integers for set A: ").split()))
B = set(map(int, input("Enter integers to remove (set B): ").split()))
A.difference_update(B)
print("A after removing elements of B:", A)
