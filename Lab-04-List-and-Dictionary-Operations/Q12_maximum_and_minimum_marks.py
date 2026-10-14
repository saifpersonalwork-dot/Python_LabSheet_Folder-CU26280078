"""Lab solution: Maximum and Minimum Marks
Question number: 12
"""

marks = {name: float(value) for name, value in (input("Enter name and marks, one pair per line; blank name ends: ").split() for _ in range(int(input("Number of students: "))))}
if marks: print("Maximum:", max(marks.values()), "Minimum:", min(marks.values()))
