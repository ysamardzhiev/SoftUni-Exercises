n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

bombs = [[int(x) for x in el.split(',')] for el in input().split()]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'upper_left': [-1, -1],
    'upper_right': [-1, 1],
    'down_left': [1, -1],
    'down_right': [1, 1],
}

for row, col in bombs:
    bomb = matrix[row][col]

    if bomb <= 0:
        continue

    for x, y in directions.values():
        r, c = row + x, col + y

        if not (0 <= r < n and 0 <= c < n):
            continue

        if matrix[r][c] <= 0:
            continue

        matrix[r][c] -= bomb

    matrix[row][col] = 0

alive_cells = []

for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] > 0:
            alive_cells.append(matrix[row_index][col_index])

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
[print(*row) for row in matrix]