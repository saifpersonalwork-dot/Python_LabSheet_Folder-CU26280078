# Find duplicate elements in a list using a set
values = input("Enter values separated by spaces: ").split()
seen = set()
duplicates = set()
for value in values:
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)
print("Duplicate elements:", duplicates)
