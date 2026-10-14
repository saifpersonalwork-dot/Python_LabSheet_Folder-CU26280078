"""Lab solution: Student Names and Marks Dictionary
Question number: 11
"""

students = {}
count = int(input("How many students? "))
for _ in range(count):
    name = input("Student name: ")
    marks = float(input("Marks: "))
    students[name] = marks
print(students)
