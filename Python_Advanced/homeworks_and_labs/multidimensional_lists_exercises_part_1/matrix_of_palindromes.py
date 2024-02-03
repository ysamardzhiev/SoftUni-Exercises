import string

rows, cols = [int(x) for x in input().split()]

alphabet = string.ascii_lowercase

for row_index in range(rows):
    for col_index in range(cols):
        print(f'{alphabet[row_index]}{alphabet[row_index + col_index]}{alphabet[row_index]}', end=' ')
    print()