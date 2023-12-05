students = {}

n = int(input())

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in students.keys():
        students[student] = []
    students[student].append(grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")