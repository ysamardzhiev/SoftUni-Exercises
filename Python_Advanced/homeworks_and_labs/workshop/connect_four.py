class FullColumnError(Exception):
    pass


class InvalidColumnError(Exception):
    pass


ROWS, COLS = 6, 7
MAX_WINNING_MOVES = 4

directions = {
    'up': [-1, 0],
    'left': [0, -1],
    'first_diagonal': [-1, -1],
    'second_diagonal': [-1, 1],
}


def print_board(board):
    [print(row) for row in board]


def check_player_pos(col, board):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            return row
    raise FullColumnError


def validate_indexes(col):
    if 0 <= col < COLS:
        return True
    raise InvalidColumnError


def is_board_full(turns):
    return COLS * ROWS < turns


def traverse_direction(row, col, searched_element, coordinates, opposite=False):
    count = 0

    for _ in range(1, MAX_WINNING_MOVES):
        if not (0 <= row < ROWS and 0 <= col < COLS) or matrix[row][col] != searched_element:
            break

        count += 1
        if opposite:
            row -= coordinates[0]
            col -= coordinates[1]
        else:
            row += coordinates[0]
            col += coordinates[1]

    return count


def win_condition(player, row, col):
    for direction, data in directions.items():
        row_index, col_index = row + data[0], col + data[1]
        row_opposite, col_opposite = row - data[0], col - data[1]

        direction_count = traverse_direction(row_index, col_index, player, data)
        opposite_direction_count = traverse_direction(row_opposite, col_opposite, player, data, opposite=True)

        if direction_count + opposite_direction_count + 1 >= MAX_WINNING_MOVES:
            return True


matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f'Player {player}, please choose a column:\n')) - 1
        validate_indexes(column)
        row = check_player_pos(column, matrix)
        matrix[row][column] = player
        turns += 1

        if win_condition(player, row, column):
            print(f'Player {player} has won the game!')
            break

        if is_board_full(turns):
            print('Board is full, no one wins.')
            exit()
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
