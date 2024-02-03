from collections import deque

rows = int(input())
commands = deque(input().split())

matrix = []

current_position = []
total_coal = 0
collected_coal = 0

for row_index in range(rows):
    row = input().split()
    matrix.append(row)

    if 's' in row:
        col_index = row.index('s')
        current_position = [row_index, col_index]
    if 'c' in row:
        total_coal += row.count('c')

while commands:
    command = commands.popleft()
    row, col = current_position

    if command == 'up' and row - 1 >= 0:
        current_position = [row - 1, col]
    elif command == 'down' and row + 1 < rows:
        current_position = [row + 1, col]
    elif command == 'left' and col - 1 >= 0:
        current_position = [row, col - 1]
    elif command == 'right' and col + 1 < rows:
        current_position = [row, col + 1]

    current_symbol = matrix[current_position[0]][current_position[1]]

    if current_symbol == 'c':
        collected_coal += 1
        matrix[current_position[0]][current_position[1]] = '*'
    elif current_symbol == 'e':
        print(f'Game over! {(current_position[0], current_position[1])}')
        exit()

if collected_coal == total_coal:
    print(f'You collected all coal! {(current_position[0], current_position[1])}')
else:
    print(f'{total_coal - collected_coal} pieces of coal left. {(current_position[0], current_position[1])}')