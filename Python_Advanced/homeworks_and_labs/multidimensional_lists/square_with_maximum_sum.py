rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

biggest_sum = 0
biggest_sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        sub_matrix_sum = matrix[row_index][col_index] + \
                        matrix[row_index][col_index+1] + \
                        matrix[row_index+1][col_index] + \
                        matrix[row_index+1][col_index+1]
        if sub_matrix_sum > biggest_sum:
            biggest_sum = sub_matrix_sum
            biggest_sub_matrix = [[matrix[row_index][col_index], matrix[row_index][col_index+1]],
                                 [matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]]

print(*biggest_sub_matrix[0])
print(*biggest_sub_matrix[1])
print(biggest_sum)