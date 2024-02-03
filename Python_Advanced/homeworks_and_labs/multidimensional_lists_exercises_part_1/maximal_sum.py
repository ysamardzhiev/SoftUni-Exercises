rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

biggest_sum = float('-inf')
biggest_sub_matrix = []

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        first_row = matrix[row_index][col_index:col_index + 3]
        second_row = matrix[row_index + 1][col_index:col_index + 3]
        third_row = matrix[row_index + 2][col_index:col_index + 3]
        sub_matrix_sum = sum(first_row + second_row + third_row)
        if sub_matrix_sum > biggest_sum:
            biggest_sum = sub_matrix_sum
            biggest_sub_matrix = [first_row, second_row, third_row]

print(f'Sum = {biggest_sum}')
print(*biggest_sub_matrix[0])
print(*biggest_sub_matrix[1])
print(*biggest_sub_matrix[2])