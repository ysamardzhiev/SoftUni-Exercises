matrix = []
rows, columns = [int(x) for x in input().split(', ')]

total_sum = 0

for i in range(rows):
    matrix.append([int(el) for el in input().split(', ')])
    total_sum += sum(matrix[i])
print(total_sum)
print(matrix)