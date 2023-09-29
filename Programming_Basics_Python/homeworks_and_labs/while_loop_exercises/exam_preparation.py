bad_grades_count = int(input())

marks_sum = 0
exercises_counter = 0
break_time = False
bad_marks_counter = 0
last_exercise = ""

exercise_name = input()

while exercise_name != 'Enough':
    exercise_mark = int(input())
    marks_sum += exercise_mark
    exercises_counter += 1
    if exercise_mark <= 4:
        bad_marks_counter += 1
        if bad_marks_counter == bad_grades_count:
            break_time = True
            break
    last_exercise = exercise_name
    exercise_name = input()

if break_time:
    print(f'You need a break, {bad_grades_count} poor grades.')
else:
    average_score = marks_sum / exercises_counter
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {exercises_counter}')
    print(f'Last problem: {last_exercise}')