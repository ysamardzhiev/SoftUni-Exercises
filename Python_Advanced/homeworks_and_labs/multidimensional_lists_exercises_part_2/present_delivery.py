presents = int(input())
size = int(input())

neighbourhood = []

santa_pos = []
nice_kids = 0

for row in range(size):
    neighbourhood.append(input().split())
    if 'S' in neighbourhood[row]:
        santa_pos = [row, neighbourhood[row].index('S')]
        neighbourhood[santa_pos[0]][santa_pos[1]] = '-'
    nice_kids += neighbourhood[row].count('V')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

happy_nice_kids = 0

command = input()
while command != "Christmas morning":
    r, c = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        command = input()
        continue

    if neighbourhood[r][c] == 'V':
        presents -= 1
        happy_nice_kids += 1

    elif neighbourhood[r][c] == 'C':
        for direction in directions:
            row, col = r + directions[direction][0], c + directions[direction][1]
            if neighbourhood[row][col] != '-':  # if code doesnt return 100%
                presents -= 1

                if neighbourhood[row][col] == 'V':
                    happy_nice_kids += 1
                neighbourhood[row][col] = '-'

                if not presents:
                    break

    neighbourhood[r][c] = '-'
    santa_pos = [r, c]

    if not presents or nice_kids == happy_nice_kids:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and nice_kids - happy_nice_kids > 0:
    print("Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if nice_kids == happy_nice_kids:
    print(f'Good job, Santa! {happy_nice_kids} happy nice kid/s.')
else:
    print(f"No presents for {nice_kids - happy_nice_kids} nice kid/s.")