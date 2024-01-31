rows = int(input())

matrix = [[char for char in input()] for _ in range(rows)]

symbol = input()

for row_index in range(rows):
    if symbol in matrix[row_index]:
        col_index = matrix[row_index].index(symbol)
        print(f'({row_index}, {col_index})')
        break
else:
    print(f'{symbol} does not occur in the matrix')