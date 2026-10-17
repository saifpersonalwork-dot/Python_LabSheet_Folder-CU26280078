# Create the power set of a given set
from itertools import combinations

items = set(input("Enter distinct items separated by spaces: ").split())
power_set = []
items_list = list(items)
for size in range(len(items_list) + 1):
    for group in combinations(items_list, size):
        power_set.append(set(group))
print("Power set:")
for subset in power_set:
    print(subset)
