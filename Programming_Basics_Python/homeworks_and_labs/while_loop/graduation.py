student_name = input()

counter = 0
grade_sum = 0
bad_grades_counter = 0

while True:
    grade = float(input())
    if grade < 4:
        bad_grades_counter += 1
        if bad_grades_counter > 1:
            current_year = counter + 1
            print(f'{student_name} has been excluded at {current_year} grade')
            break
        continue
    else:
        grade_sum += grade
        counter += 1
    if counter == 12:
        average_score = grade_sum / counter
        print(f'{student_name} graduated. Average grade: {average_score:.2f}')
        break
