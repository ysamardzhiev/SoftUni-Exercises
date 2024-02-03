n = int(input())

diagonals = [[], []]

for row_index in range(n):
    row = [int(x) for x in input().split(', ')]
    diagonals[0].append(row[row_index])
    diagonals[1].append(row[n - row_index - 1])

print(f'Primary diagonal: {", ".join(str(x) for x in diagonals[0])}. Sum: {sum(diagonals[0])}')
print(f'Secondary diagonal: {", ".join(str(x) for x in diagonals[1])}. Sum: {sum(diagonals[1])}')