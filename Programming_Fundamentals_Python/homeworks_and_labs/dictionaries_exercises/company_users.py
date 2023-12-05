company_employees = {}

command = input()
while command != 'End':
    company, employee_id = command.split(' -> ')
    if company not in company_employees.keys():
        company_employees[company] = []
    if employee_id not in company_employees[company]:
        company_employees[company].append(employee_id)
    command = input()

for company, employees in company_employees.items():
    print(company)
    for employee in employees:
        print(f'-- {employee}')