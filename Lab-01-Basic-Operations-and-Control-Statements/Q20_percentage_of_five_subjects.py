"""Lab solution: Percentage of Five Subjects
Question number: 20
"""

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Marks in subject {i} (out of 100): ")))
print("Percentage:", sum(marks) / 5, "%")
