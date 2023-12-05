from math import ceil

people_count = int(input())
elevator_capacity = int(input())

courses_needed = ceil(people_count / elevator_capacity)
print(courses_needed)

