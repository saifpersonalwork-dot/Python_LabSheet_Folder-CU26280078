# Remove duplicates from a list using a set
values = input("Enter values separated by spaces: ").split()
unique_values = list(set(values))
print("List after removing duplicates (order may change):", unique_values)
