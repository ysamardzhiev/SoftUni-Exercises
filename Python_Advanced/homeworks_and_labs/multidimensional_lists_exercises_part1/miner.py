from collections import deque


def find_starting_position(matrix, row_count):
    for row_index in range(row_count):
        if 's' in matrix[row_index]:
            col_index = matrix[row_index].index('s')
            return [row_index, col_index]


def find_all_coal(matrix, row_count):
    all_coal = 0
    for row_index in range(row_count):
        all_coal += matrix[row_index].count('c')
    return all_coal


rows = int(input())
commands = deque(input().split())

field = [input().split() for _ in range(rows)]

current_position = find_starting_position(field, rows)
total_coal = find_all_coal(field, rows)
collected_coal = 0

while commands:
    command = commands.popleft()
    row, col = current_position
    current_symbol = ''
    if command == 'up' and row - 1 >= 0:
        current_symbol = field[row - 1][col]
        current_position = [row - 1, col]
    elif command == 'down' and row + 1 < rows:
        current_symbol = field[row + 1][col]
        current_position = [row + 1, col]
    elif command == 'left' and col - 1 >= 0:
        current_symbol = field[row][col - 1]
        current_position = [row, col - 1]
    elif command == 'right' and col + 1 < rows:
        current_symbol = field[row][col + 1]
        current_position = [row, col + 1]

    if current_symbol == 'c':
        collected_coal += 1
        field[current_position[0]][current_position[1]] = '*'
    elif current_symbol == 'e':
        print(f'Game over! {(current_position[0], current_position[1])}')
        exit()
if collected_coal == total_coal:
    print(f'You collected all coal! {(current_position[0], current_position[1])}')
else:
    print(f'{total_coal - collected_coal} pieces of coal left. {(current_position[0], current_position[1])}')