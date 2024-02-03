rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

found_squares = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        first_el = matrix[row_index][col_index]
        second_el = matrix[row_index][col_index + 1]
        third_el = matrix[row_index + 1][col_index]
        fourth_el = matrix[row_index + 1][col_index + 1]
        if first_el == second_el == third_el == fourth_el:
            found_squares += 1
print(found_squares)