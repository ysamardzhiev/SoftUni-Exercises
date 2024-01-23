students_count = int(input())

student_record = {}

for _ in range(students_count):
    name, grade = input().split()
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(float(grade))

for student, grades in student_record.items():
    average_grade = sum(grades) / len(grades)
    grades = [f'{grade:.2f}' for grade in grades]
    print(f'{student} -> {" ".join(grades)} (avg: {average_grade:.2f})')