fire_levels = input().split('#')
amount_of_water = int(input())

put_out_cells = []

for current_fire_level in fire_levels:
    type_of_fire, cell_value = current_fire_level.split(' = ')
    cell_value = int(cell_value)
    if amount_of_water >= cell_value:
        if type_of_fire == 'High':
            if 81 <= cell_value <= 125:
                amount_of_water -= cell_value
                put_out_cells.append(cell_value)
        elif type_of_fire == 'Medium':
            if 51 <= cell_value <= 80:
                amount_of_water -= cell_value
                put_out_cells.append(cell_value)
        elif type_of_fire == 'Low':
            if 1 <= cell_value <= 50:
                amount_of_water -= cell_value
                put_out_cells.append(cell_value)
total_effort = sum(put_out_cells) * 0.25

# PRINTING RESULTS
print('Cells:')
for current_value in put_out_cells:
    print(f'- {current_value}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {sum(put_out_cells)}')