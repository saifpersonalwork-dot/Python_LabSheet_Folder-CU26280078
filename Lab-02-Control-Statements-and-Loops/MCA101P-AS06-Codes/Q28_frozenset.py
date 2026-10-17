# Create a frozenset and demonstrate its properties
values = input("Enter values separated by spaces: ").split()
frozen = frozenset(values)
print("Frozenset:", frozen)
print("Number of elements:", len(frozen))
print("Contains 'Python':", "Python" in frozen)
print("A frozenset is immutable and has no add() method.")
