rows, cols = [int(x) for x in input().split()]

neighbourhood = []

starting_pos = []

for row in range(rows):
    line = list(input())
    neighbourhood.append(line)

    if 'B' in line:
        col = line.index('B')
        starting_pos = [row, col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

boy_pos = [starting_pos[0], starting_pos[1]]

while True:
    direction = input()
    r, c = boy_pos[0] + directions[direction][0], boy_pos[1] + directions[direction][1]

    if not (0 <= r < rows and 0 <= c < cols):
        print("The delivery is late. Order is canceled.")
        neighbourhood[starting_pos[0]][starting_pos[1]] = ' '
        break

    symbol = neighbourhood[r][c]

    if symbol == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        neighbourhood[r][c] = 'R'
    elif symbol == 'A':
        print("Pizza is delivered on time! Next order...")
        neighbourhood[r][c] = 'P'
        break
    elif symbol == '-':
        neighbourhood[r][c] = '.'
    elif symbol == '*':
        continue

    boy_pos = [r, c]

[print(*row, sep='') for row in neighbourhood]