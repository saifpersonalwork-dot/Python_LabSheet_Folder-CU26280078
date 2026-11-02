# Q20: Find the Cartesian product of two sets
set_a = {1, 2}
set_b = {"A", "B"}
product = {(a, b) for a in set_a for b in set_b}
print("Cartesian product:", product)
