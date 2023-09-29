season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

price = 0
sport = ""

if season == 'Winter':
    if type_of_group == 'girls':
        price = 9.60 * nights_count * students_count
        sport = 'Gymnastics'
    elif type_of_group == 'boys':
        price = 9.60 * nights_count * students_count
        sport = 'Judo'
    elif type_of_group == 'mixed':
        price = 10 * nights_count * students_count
        sport = 'Ski'
elif season == 'Spring':
    if type_of_group == 'girls':
        price = 7.20 * nights_count * students_count
        sport = 'Athletics'
    elif type_of_group == 'boys':
        price = 7.20 * nights_count * students_count
        sport = 'Tennis'
    elif type_of_group == 'mixed':
        price = 9.50 * nights_count * students_count
        sport = 'Cycling'
elif season == 'Summer':
    if type_of_group == 'girls':
        price = 15 * nights_count * students_count
        sport = 'Volleyball'
    elif type_of_group == 'boys':
        price = 15 * nights_count * students_count
        sport = 'Football'
    elif type_of_group == 'mixed':
        price = 20 * nights_count * students_count
        sport = 'Swimming'

if students_count >= 50:
    price = price * 0.5
elif 20 <= students_count < 50:
    price = price * 0.85
elif 10 <= students_count < 20:
    price = price * 0.95

print(f'{sport} {price:.2f} lv.')