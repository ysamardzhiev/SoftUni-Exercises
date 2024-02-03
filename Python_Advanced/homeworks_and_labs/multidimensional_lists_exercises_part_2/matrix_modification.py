n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

command = input()
while command != 'END':
    action, *data = command.split()
    row, col, value = [int(x) for x in data]

    if not (0 <= row < n and 0 <= col < n):
        print('Invalid coordinates')
        command = input()
        continue

    if action == 'Add':
        matrix[row][col] += value
    elif action == 'Subtract':
        matrix[row][col] -= value

    command = input()

[print(*row) for row in matrix]