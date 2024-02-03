rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

command = input()
while command != 'END':
    commands = command.split()
    if commands[0] == 'swap' and len(commands) == 5:
        coordinates = [int(x) for x in commands[1:]]
        row1, col1, row2, col2 = coordinates
        if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()