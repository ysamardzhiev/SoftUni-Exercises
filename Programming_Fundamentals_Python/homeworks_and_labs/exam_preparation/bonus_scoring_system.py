number_of_students = int(input())
lectures_count = int(input())
additional_bonus = int(input())

most_attended_lectures = 0
last_max_bonus = 0

for student in range(number_of_students):
    student_attendance = int(input())
    max_bonus = round(student_attendance / lectures_count * (5 + additional_bonus))
    if max_bonus > last_max_bonus:
        last_max_bonus = max_bonus
        most_attended_lectures = student_attendance

print(f"Max Bonus: {last_max_bonus}.\n"
      f"The student has attended {most_attended_lectures} lectures.")