"""Lab solution: Largest and Smallest in List
Question number: 21
"""

numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
if not numbers: print("List is empty")
else:
    smallest = largest = numbers[0]
    for n in numbers[1:]:
        if n < smallest: smallest = n
        if n > largest: largest = n
    print("Smallest:", smallest, "Largest:", largest)
