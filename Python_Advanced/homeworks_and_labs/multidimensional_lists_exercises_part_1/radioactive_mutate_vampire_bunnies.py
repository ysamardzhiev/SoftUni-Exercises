import copy

rows, cols = [int(x) for x in input().split()]

lair = []

player_pos = []

for row in range(rows):
    line = list(input())
    lair.append(line)
    if 'P' in line:
        col = line.index('P')
        player_pos = [row, col]

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

lair_copy = copy.deepcopy(lair)
commands = [letter for letter in input()]

for command in commands:
    for row in range(rows):
        for col in range(cols):
            if 'B' not in lair[row]:
                break
            elif 'B' not in lair[row][col]:
                continue

            for direction in directions:
                bunny_r, bunny_c = row + directions[direction][0], col + directions[direction][1]

                if not (0 <= bunny_r < rows and 0 <= bunny_c < cols):
                    continue

                if lair[bunny_r][bunny_c] == 'P':
                    [print(*row, sep='') for row in lair]
                    print(f'dead: {bunny_r} {bunny_c}')
                    exit()
                lair_copy[bunny_r][bunny_c] = 'B'
    lair = lair_copy

    r, c = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        [print(*row, sep='') for row in lair]
        print(f'won: {player_pos[0]} {player_pos[1]}')
        exit()

    if lair[r][c] == 'B':
        [print(*row, sep='') for row in lair]
        print(f'dead: {r} {c}')
        exit()

    lair[r][c] = 'P'
    player_pos = [r, c]