size = int(input())

matrix = []

knights_indexes = []

for row_index in range(size):
    row = [el for el in input()]
    matrix.append(row)
    for col_index in range(size):
        if 'K' in matrix[row_index][col_index]:
            knights_indexes.append([row_index, col_index])

knight_moves = (
    (-2, -1),  # top left vertical
    (-2, 1),  # top right vertical
    (-1, -2),  # top left horizontal
    (-1, 2),  # top right horizontal
    (2, -1),  # bottom left vertical
    (2, 1),  # bottom right vertical
    (1, -2),  # bottom left horizontal
    (1, 2),  # bottom right horizontal
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks = []
    for row, col in knights_indexes:
        attacks_count = 0
        for x, y in knight_moves:
            r, c = row + x, col + y

            if not (0 <= r < size and 0 <= c < size):
                continue
            elif matrix[r][c] == 'K':
                attacks_count += 1

        if attacks_count > max_attacks:
            max_attacks = attacks_count
            knight_with_most_attacks = [row, col]

    if knight_with_most_attacks:
        r, c = knight_with_most_attacks
        knights_indexes.remove([r, c])
        matrix[r][c] = '0'
        removed_knights += 1
    else:
        break
print(removed_knights)