"""Lab solution: Body Mass Index
Question number: 18
"""

weight = float(input("Weight in kg: "))
height = float(input("Height in metres: "))
if height <= 0:
    print("Height must be greater than zero.")
else:
    print("BMI:", round(weight / (height ** 2), 2))
