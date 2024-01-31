rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
diagonal_sum = 0

for row_index in range(len(matrix)):
    for col_index in range(len(matrix)):
        if row_index == col_index:
            diagonal_sum += matrix[row_index][col_index]
            break
print(diagonal_sum)