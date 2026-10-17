# Remove an element using remove()
items = {10, 20, 30, 40}
try:
    value = int(input("Enter the number to remove: "))
    items.remove(value)
    print("Updated set:", items)
except ValueError:
    print("That element is not in the set or is not a valid integer.")
