size = int(input())

airspace = []

jet_pos = []
enemy_planes = 4
armor = 300

for row in range(size):
    line = list(input())
    airspace.append(line)

    if 'J' in line:
        col = line.index('J')
        jet_pos = [row, col]
        airspace[row][col] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while armor > 0 and enemy_planes:
    direction = input()
    r, c = jet_pos[0] + directions[direction][0], jet_pos[1] + directions[direction][1]

    symbol = airspace[r][c]
    airspace[r][c] = '-'
    jet_pos = [r, c]

    if symbol == 'E':
        enemy_planes -= 1
        if enemy_planes:
            armor -= 100
    elif symbol == 'R':
        armor = 300

airspace[jet_pos[0]][jet_pos[1]] = 'J'

if not enemy_planes:
    print("Mission accomplished, you neutralized the aerial threat!")
elif not armor:
    print(f'Mission failed, your jetfighter was shot down! Last coordinates [{jet_pos[0]}, {jet_pos[1]}]!')

[print(*row, sep='') for row in airspace]