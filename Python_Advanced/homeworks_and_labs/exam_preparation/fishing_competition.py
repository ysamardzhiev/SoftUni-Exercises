size = int(input())

fishing_area = []

my_pos = []

for row in range(size):
    line = list(input())
    fishing_area.append(line)
    if 'S' in line:
        col = line.index('S')
        my_pos = [row, col]
        fishing_area[row][col] = '-'

directions = {
    'up': ((-1, 0), (size, 0)),
    'down': ((1, 0), (-size, 0)),
    'left': ((0, -1), (0, size)),
    'right': ((0, 1), (0, -size))
}

quota = 20
collected_fish = 0

command = input()
while command != 'collect the nets':
    r, c = my_pos[0] + directions[command][0][0], my_pos[1] + directions[command][0][1]

    if not (0 <= r < size and 0 <= c < size):
        r += directions[command][1][0]
        c += directions[command][1][1]

    element = fishing_area[r][c]

    if element == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{r},{c}]")
        exit()
    elif element.isdigit():
        collected_fish += int(element)
        fishing_area[r][c] = '-'

    my_pos = [r, c]
    command = input()

fishing_area[my_pos[0]][my_pos[1]] = 'S'

if collected_fish >= quota:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {quota - collected_fish} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*row, sep='') for row in fishing_area]