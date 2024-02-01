rows_and_cols = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows_and_cols)]
diagonals = [[], []]

for row_index in range(len(matrix)):
    diagonals[0].append(matrix[row_index][row_index])

row_index = 0
for col_index in range(len(matrix) - 1, -1, -1):
    diagonals[1].append(matrix[row_index][col_index])
    row_index += 1

print(f'Primary diagonal: {", ".join(str(x) for x in diagonals[0])}. Sum: {sum(diagonals[0])}')
print(f'Secondary diagonal: {", ".join(str(x) for x in diagonals[1])}. Sum: {sum(diagonals[1])}')