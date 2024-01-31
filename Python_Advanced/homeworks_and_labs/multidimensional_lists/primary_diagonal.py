rows = int(input())

diagonal_sum = 0

for row_index in range(rows):
    row_data = [int(x) for x in input().split()]
    diagonal_sum += row_data[row_index]
print(diagonal_sum)