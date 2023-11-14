students_information = {}

students_count = 1

data = input()
while ':' in data:
    name, student_id, course = data.split(':')
    students_information[students_count] = {}
    students_information[students_count]['name'] = name
    students_information[students_count]['ID'] = int(student_id)
    students_information[students_count]['course'] = course

    students_count += 1
    data = input()

data = data.replace('_', ' ')
for current_student in range(1, students_count):
    if data in students_information[current_student].values():
        print(f'{students_information[current_student]["name"]} - {students_information[current_student]["ID"]}')