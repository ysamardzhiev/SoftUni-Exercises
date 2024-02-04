size = int(input())

matrix = []

alice_pos = []

for row_index in range(size):
    matrix.append(input().split())
    if 'A' in matrix[row_index]:
        col_index = matrix[row_index].index('A')
        alice_pos = [row_index, col_index]
        matrix[row_index][col_index] = '*'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

collected_tea_bags = 0


command = input()
row, col = alice_pos[0] + directions[command][0], alice_pos[1] + directions[command][1]

while 0 <= row < size and 0 <= col < size:

    if matrix[row][col] == 'R':
        print("Alice didn't make it to the tea party.")
        matrix[row][col] = '*'
        break

    collected_tea_bags += int(matrix[row][col]) if matrix[row][col].isdigit() else 0
    matrix[row][col] = '*'

    if collected_tea_bags >= 10:
        print('She did it! She went to the party.')
        break

    command = input()

    row += directions[command][0]
    col += directions[command][1]
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]