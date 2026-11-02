# Q19: Create the power set of a given set
my_set = {1, 2, 3}
power_set = {frozenset()}

for element in my_set:
    new_subsets = set()
    for subset in power_set:
        new_subsets.add(subset | {element})
    power_set.update(new_subsets)

print("Power set:")
for subset in power_set:
    print(set(subset))
