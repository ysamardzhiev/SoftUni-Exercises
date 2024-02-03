n = int(input())

primary_sum, secondary_sum = 0, 0

for row_index in range(n):
    row = [int(el) for el in input().split()]
    primary_sum += row[row_index]
    secondary_sum += row[n - row_index - 1]

print(abs(primary_sum - secondary_sum))