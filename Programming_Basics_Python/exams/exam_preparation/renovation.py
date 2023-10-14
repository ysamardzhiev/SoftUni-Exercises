from math import ceil

height_wall = int(input())
width_wall = int(input())
no_paint_percent = int(input())

total_area = height_wall * width_wall * 4
walls_to_paint = ceil(total_area - (total_area * no_paint_percent / 100))

input_line = input()
while input_line != 'Tired!':
    paint_liters = int(input_line)
    walls_to_paint = walls_to_paint - paint_liters

    if walls_to_paint < 0:
        walls_to_paint = abs(walls_to_paint)
        print(f'All walls are painted and you have {int(walls_to_paint)} l paint left!')
        break
    elif walls_to_paint == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break
    input_line = input()
else:
    print(f'{int(walls_to_paint)} quadratic m left.')