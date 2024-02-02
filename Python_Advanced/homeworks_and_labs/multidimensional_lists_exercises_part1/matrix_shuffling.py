rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

command = input()
while command != 'END':
    commands = command.split()
    if commands[0] == 'swap':
        coordinates = [int(x) for x in commands[1:]]
        if len(coordinates) == 4:
            row1, col1, row2, col2 = coordinates
            if row1 < rows and row2 < rows and col1 < cols and col2 < cols:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                [print(*row) for row in matrix]
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()