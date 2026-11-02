# Q4: Add multiple elements to a set
my_set = {10, 20, 30}
items = input("Enter multiple elements separated by spaces: ").split()
my_set.update(items)
print("Updated set:", my_set)
