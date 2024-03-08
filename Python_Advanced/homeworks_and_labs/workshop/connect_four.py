class FullColumnError(Exception):
    pass


class InvalidColumnError(Exception):
    pass


ROWS, COLS = 6, 7


def print_board(board):
    [print(row) for row in board]


def check_player_pos(player, col, board):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return
    raise FullColumnError


def validate_indexes(col):
    if 0 <= col < COLS:
        return True
    raise InvalidColumnError


matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f'Player {player}, please choose a column:\n')) - 1
        validate_indexes(column)
        check_player_pos(player, column, matrix)
    except FullColumnError:
        print('This column is full! Try with another one.')
        continue
    except InvalidColumnError:
        print(f'Out of the board! Please select a number between 1 and {COLS}!')
        continue
    except ValueError:
        print(f'Invalid number! Please select a number between 1 and {COLS}!')
        continue

    print_board(matrix)
    turns += 1