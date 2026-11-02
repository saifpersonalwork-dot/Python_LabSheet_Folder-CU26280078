# Q21: Count distinct elements from a list using a set
numbers = input("Enter numbers separated by spaces: ").split()
distinct = set(numbers)
print("Distinct elements:", distinct)
print("Count of distinct elements:", len(distinct))
