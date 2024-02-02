import string

rows, cols = [int(x) for x in input().split()]

alphabet = list(string.ascii_lowercase)
matrix = []


for row_index in range(rows):
    matrix.append([])
    for col_index in range(cols):
        matrix[row_index].append(f'{alphabet[row_index]}{alphabet[row_index + col_index]}{alphabet[row_index]}')

[print(*row) for row in matrix]