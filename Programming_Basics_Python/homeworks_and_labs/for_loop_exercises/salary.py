open_tabs = int(input())
salary = float(input())

for tab in range(1, open_tabs + 1):
    tab_name = input()
    if tab_name == 'Facebook':
        salary -= 150
    elif tab_name == 'Instagram':
        salary -= 100
    elif tab_name == 'Reddit':
        salary -= 50
    elif salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(int(salary))