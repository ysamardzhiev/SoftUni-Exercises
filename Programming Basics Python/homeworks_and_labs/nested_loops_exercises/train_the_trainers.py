jury_count = int(input())

counter = 0
total_marks_sum = 0

input_line = input()
while input_line != 'Finish':
    mark_sum = 0
    for grades in range(jury_count):
        presentation_mark = float(input())
        counter += 1
        mark_sum += presentation_mark
        total_marks_sum += presentation_mark

    presentation_total_mark = mark_sum / jury_count
    print(f'{input_line} - {presentation_total_mark:.2f}.')
    input_line = input()
total_grade = total_marks_sum / counter
print(f"Student's final assessment is {total_grade:.2f}.")