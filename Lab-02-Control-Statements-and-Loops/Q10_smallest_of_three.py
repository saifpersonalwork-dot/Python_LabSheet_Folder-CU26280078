"""Lab solution: Smallest of Three
Question number: 10
"""

numbers = [float(input(f"Number {i}: ")) for i in range(1, 4)]
smallest = numbers[0]
for number in numbers[1:]:
    if number < smallest:
        smallest = number
print("Smallest:", smallest)
