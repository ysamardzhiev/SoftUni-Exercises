students_information = []

data = input()
while ':' in data:
    name, student_id, course = data.split(':')
    students_information.append({'name': name, 'ID': student_id, 'course': course})
    data = input()

searched_course = data.replace('_', ' ')
for current_student in students_information:
    if searched_course in current_student['course']:
        print(f'{current_student["name"]} - {current_student["ID"]}')