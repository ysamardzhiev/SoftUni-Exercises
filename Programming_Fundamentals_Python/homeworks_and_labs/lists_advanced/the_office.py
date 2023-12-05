employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())

employees_ratings = [current_employee * happiness_improvement_factor for current_employee in employees_happiness]
average_rating = sum(employees_ratings) / len(employees_ratings)

happy_employees_list = list(filter(lambda x: x >= average_rating, employees_ratings))

if len(happy_employees_list) >= len(employees_ratings) // 2:
    print(f'Score: {len(happy_employees_list)}/{len(employees_ratings)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees_list)}/{len(employees_ratings)}. Employees are not happy!')