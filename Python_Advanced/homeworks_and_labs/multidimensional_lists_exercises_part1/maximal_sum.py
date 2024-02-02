rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

biggest_sum = float('-inf')
biggest_sub_matrix = []

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        first_el = matrix[row_index][col_index]
        second_el = matrix[row_index][col_index + 1]
        third_el = matrix[row_index][col_index + 2]
        fourth_el = matrix[row_index + 1][col_index]
        fifth_el = matrix[row_index + 1][col_index + 1]
        sixth_el = matrix[row_index + 1][col_index + 2]
        seventh_el = matrix[row_index + 2][col_index]
        eighth_el = matrix[row_index + 2][col_index + 1]
        ninth_el = matrix[row_index + 2][col_index + 2]
        sub_matrix_sum = first_el + second_el + third_el \
                         + fourth_el + fifth_el + sixth_el \
                         + seventh_el + eighth_el + ninth_el
        if sub_matrix_sum > biggest_sum:
            biggest_sum = sub_matrix_sum
            biggest_sub_matrix = [[first_el, second_el, third_el], [fourth_el, fifth_el, sixth_el], [seventh_el, eighth_el, ninth_el]]

print(f'Sum = {biggest_sum}')
print(*biggest_sub_matrix[0])
print(*biggest_sub_matrix[1])
print(*biggest_sub_matrix[2])