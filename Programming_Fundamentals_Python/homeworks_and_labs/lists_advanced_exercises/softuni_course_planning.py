def add_lessons():
    if lesson_title not in lessons:
        lessons.append(lesson_title)


def insert_lessons():
    index = int(command[2])
    if lesson_title not in lessons:
        lessons.insert(index, lesson_title)


def remove_lessons():
    if lesson_title in lessons:
        lessons.remove(lesson_title)
        if lesson_exercise in lessons:
            lessons.remove(lesson_exercise)


def swap_lessons():
    second_lesson = command[2]
    second_lesson_exercise = f'{second_lesson}-Exercise'
    if lesson_title in lessons and second_lesson in lessons:
        first_index = lessons.index(lesson_title)
        second_index = lessons.index(second_lesson)
        lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
        if lesson_exercise in lessons:
            lessons.remove(lesson_exercise)
            lessons.insert(second_index + 1, lesson_exercise)
        elif second_lesson_exercise in lessons:
            lessons.remove(second_lesson_exercise)
            lessons.insert(first_index + 1, second_lesson_exercise)


def add_exercise():
    if lesson_title not in lessons:
        lessons.append(lesson_title)
        lessons.append(lesson_exercise)
    elif lesson_title in lessons and lesson_exercise not in lessons:
        lesson_index = lessons.index(lesson_title)
        lessons.insert(lesson_index + 1, lesson_exercise)


lessons = input().split(', ')

command_line = input()
while command_line != 'course start':
    command = command_line.split(':')
    type_of_command = command[0]
    lesson_title = command[1]
    lesson_exercise = f'{lesson_title}-Exercise'
    if type_of_command == 'Add':
        add_lessons()
    elif type_of_command == 'Insert':
        insert_lessons()
    elif type_of_command == 'Remove':
        remove_lessons()
    elif type_of_command == 'Swap':
        swap_lessons()
    elif type_of_command == 'Exercise':
        add_exercise()
    command_line = input()
formatted_lessons = [f'{index + 1}.{lessons[index]}' for index in range(len(lessons))]
print('\n'.join(formatted_lessons))