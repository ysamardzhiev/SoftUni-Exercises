class FullColumnError(Exception):
    pass


def print_board(board):
    [print(row) for row in board]


def check_player_pos(player, col, board):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return
    raise FullColumnError


def win_condition(player, row, col, board):
    pass


ROWS, COLS = 6, 7

matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1
    
    try:
        column = int(input(f'Player {player}, please choose a column:\n')) - 1
    except ValueError:
        print('Invalid number')
        continue

    if column >= COLS:
        print('Out of the board! Try again!')
        continue

    try:
        check_player_pos(player, column, matrix)
    except FullColumnError:
        print('This column is full! Try with another one.')
        continue

    print_board(matrix)

    turns += 1