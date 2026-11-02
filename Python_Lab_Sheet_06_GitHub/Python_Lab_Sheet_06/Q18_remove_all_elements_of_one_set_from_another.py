# Q18: Remove all elements of B from A
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4}
set_a.difference_update(set_b)
print("A after removing elements of B:", set_a)
