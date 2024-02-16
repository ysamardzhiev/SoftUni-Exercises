size = int(input())

game_board = []

gambler_pos = None

for row in range(size):
    line = [x for x in input()]
    game_board.append(line)
    if 'G' in line:
        col = line.index('G')
        gambler_pos = [row, col]
        game_board[row][col] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

total_amount = 100

command = input()
while command != 'end':
    r, c = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        print("Game over! You lost everything!")
        exit()

    symbol = game_board[r][c]
    game_board[r][c] = '-'
    gambler_pos = [r, c]

    if symbol == 'W':
        total_amount += 100
    elif symbol == 'P':
        total_amount -= 200
    elif symbol == 'J':
        total_amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {total_amount}$")
        break

    if total_amount <= 0:
        print("Game over! You lost everything!")
        exit()

    command = input()
else:
    print(f"End of the game. Total amount: {total_amount}$")

game_board[gambler_pos[0]][gambler_pos[1]] = 'G'

[print(*row, sep='') for row in game_board]