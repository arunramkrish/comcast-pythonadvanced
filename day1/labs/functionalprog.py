students = [
    {'name': 'Alice', 'grade': 'A', 'age': 30},
    {'name': 'Bob', 'grade': 'B', 'age': 40},
    {'name': 'Charlie', 'grade': 'C', 'age':20}
]

sorted_students = sorted(students, key=lambda student: student['age'] * -1)
print(sorted_students)
