lenght = float(input())
width = float(input())

desk_space = (width * 100) - 100
desks_per_row = desk_space // 70
row = (lenght * 100) // 120

total_places = row * desks_per_row - 3
print(f'{total_places}')
