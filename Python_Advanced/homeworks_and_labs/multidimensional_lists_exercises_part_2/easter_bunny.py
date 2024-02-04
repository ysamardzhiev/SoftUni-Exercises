size = int(input())

matrix = []

bunny_pos = []

for row_index in range(size):
    matrix.append(input().split())
    if 'B' in matrix[row_index]:
        bunny_pos = [row_index, matrix[row_index].index('B')]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

max_collected_eggs = float('-inf')
best_direction = ''
best_path = []

for direction, positions in directions.items():
    r, c = bunny_pos[0] + positions[0], bunny_pos[1] + positions[1]
    collected_eggs = 0
    path = []

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'X':
            break

        collected_eggs += int(matrix[r][c])
        path.append([r, c])

        r += positions[0]
        c += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
[print(row) for row in best_path]
print(max_collected_eggs)