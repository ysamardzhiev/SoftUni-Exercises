rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

biggest_sum = 0
biggest_submatrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        submatrix_sum = matrix[row_index][col_index] + \
                        matrix[row_index][col_index+1] + \
                        matrix[row_index+1][col_index] + \
                        matrix[row_index+1][col_index+1]
        if submatrix_sum > biggest_sum:
            biggest_sum = submatrix_sum
            biggest_submatrix = [[matrix[row_index][col_index], matrix[row_index][col_index+1]],
                                 [matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]]

for row in biggest_submatrix:
    print(*row)
print(biggest_sum)