"""Lab solution: Check if List Is Sorted
Question number: 07
"""

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Sorted in ascending order" if all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1)) else "Not sorted")
