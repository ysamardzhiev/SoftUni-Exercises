rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col_index in range(columns):
    column_sum = 0
    for row_index in range(len(matrix)):
        column_sum += matrix[row_index][col_index]
    print(column_sum)