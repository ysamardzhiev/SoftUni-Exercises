import speech_recognition as sr

from pyfiglet import Figlet


class InvalidNumber(Exception):
    pass


class InvalidSymbol(Exception):
    pass


class PositionNotAvailable(Exception):
    pass


BOARD_SIZE = 3
WINNING_MOVES = 3

NUM_OPERATIONS = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

DIRECTIONS = {
    'up': (-1, 0),
    'left': (0, -1),
    'first_diagonal': (-1, -1),
    'second_diagonal': (-1, 1),
}


def traverse_direction(row, col, matrix, searched_symbol, coordinates,opposite=False):
    count = 0
    for _ in range(WINNING_MOVES):
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE) or matrix[row][col] != searched_symbol:
            break

        count += 1
        if opposite:
            row -= coordinates[0]
            col -= coordinates[1]
        else:
            row += coordinates[0]
            col += coordinates[1]

    return count


def winning_position(game_board, row, col, symbol):
    for direction, data in DIRECTIONS.items():
        row_index, col_index = row + data[0], col + data[1]
        row_opposite, col_opposite = row - data[0], col - data[1]

        dir_count = traverse_direction(row_index, col_index, game_board, symbol, data)
        reverse_dir_count = traverse_direction(row_opposite, col_opposite, game_board, symbol, data, opposite=True)

        if dir_count + reverse_dir_count + 1 == WINNING_MOVES:
            return True
    return False


def print_user_interface(first_player):
    print('This is the numeration of the board:')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')
    print(f'{first_player} starts first!')


def print_board(game_board):
    [print(f'|  {"  |  ".join(row)}  |') for row in game_board]


def is_valid_number(player_choice):
    if player_choice in NUM_OPERATIONS:
        return NUM_OPERATIONS[player_choice]
    raise InvalidNumber


def is_symbol_valid(player_symbol):
    if player_symbol == 'X' or player_symbol == 'O':
        return 'O' if player_symbol == 'X' else 'X'
    raise InvalidSymbol


def is_position_available(game_board, row_index, col_index):
    symbol = game_board[row_index][col_index]
    if symbol == 'X' or symbol == 'O':
        raise PositionNotAvailable
    return True


def is_board_full(turns_count):
    return BOARD_SIZE * BOARD_SIZE <= turns_count


def is_name_valid(player1, player2):
    return player1.lower() == player2.lower()


def get_names(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f'Player {player_number} please say your name: ')

            audio = r.record(source, duration=3)
            print('Recognizing...')

            try:
                return r.recognize_google(audio)
            except sr.exceptions.UnknownValueError:
                print("Didn't hear you well, please say your name again!")


f = Figlet(font='slant')
print(f.renderText('Tic Tac Toe'))

while True:
    player_one = get_names(1)
    player_two = get_names(2)

    if is_name_valid(player_one, player_two):
        print('Names must not be identical! Please choose another name!')
        continue
    print(f'{player_one} and {player_two} will face against each other!')
    break

board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

players = {player_one: None, player_two: None}

turns = 1

while True:
    if turns == 1:
        player1_symbol = input(f'{player_one} would you like to play with "X" or "O": ').capitalize()

        try:
            player2_symbol = is_symbol_valid(player1_symbol)
        except InvalidSymbol:
            print(f'Please choose between "X" and "O"!')
            continue

        players[player_one] = player1_symbol
        players[player_two] = player2_symbol
        print_user_interface(player_one)

    current_player = player_one if turns % 2 else player_two
    current_symbol = players[current_player]

    try:
        player_pos = int(input(f'{current_player} choose a free position from 1 to 9: '))
        row, col = is_valid_number(player_pos)

        if is_position_available(board, row, col):
            board[row][col] = current_symbol

        if is_board_full(turns):
            print('The board is full! DRAW!')
            exit(0)

        if winning_position(board, row, col, current_symbol):
            print(f'The game is over! The winner is {current_player}!')
            exit(0)

    except (ValueError, InvalidNumber):
        print('Please enter a number from 1 to 9!')
        continue
    except PositionNotAvailable:
        print('This position is already taken! Choose another one.')
        continue

    print_board(board)
    turns += 1