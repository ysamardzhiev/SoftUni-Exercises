size = 5

matrix = []

shooting_pos = []

total_targets = 0
found_targets = []

for row_index in range(size):
    matrix.append(input().split())
    if 'A' in matrix[row_index]:
        shooting_pos = [row_index, matrix[row_index].index('A')]
    if 'x' in matrix[row_index]:
        total_targets += matrix[row_index].count('x')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

n = int(input())

for _ in range(n):
    commands = input().split()
    type_of_command, direction = commands[0], commands[1]
    row, col = shooting_pos[0], shooting_pos[1]

    if type_of_command == 'move':
        steps = int(commands[2])
        row = shooting_pos[0] + directions[direction][0] * steps
        col = shooting_pos[1] + directions[direction][1] * steps
        if not (0 <= row < size and 0 <= col < size):
            row, col = shooting_pos
        elif matrix[row][col] != '.':
            row, col = shooting_pos
        shooting_pos = [row, col]

    elif type_of_command == 'shoot':
        while 0 <= row < size and 0 <= col < size:
            if matrix[row][col] == 'x':
                found_targets.append([row, col])
                total_targets -= 1
                matrix[row][col] = '.'
                break
            row += directions[direction][0]
            col += directions[direction][1]

        if not total_targets:
            print(f"Training completed! All {len(found_targets)} targets hit.")
            break
else:
    print(f'Training not completed! {total_targets} targets left.')

print(*found_targets, sep='\n')