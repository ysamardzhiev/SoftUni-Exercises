rows = int(input())

diagonal_sum = 0

for row_index in range(rows):
    row_data = [int(x) for x in input().split()]
    for col_index in range(rows):
        if row_index == col_index:
            diagonal_sum += row_data[col_index]
            break
print(diagonal_sum)