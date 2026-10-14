"""Lab solution: Leap Year
Question number: 24
"""

year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
