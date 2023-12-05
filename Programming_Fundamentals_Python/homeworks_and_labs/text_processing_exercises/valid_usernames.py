def length_check(some_username):
    if 3 <= len(some_username) <= 16:
        return True


def symbols_check(some_username):
    for char in some_username:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def redundant_check(some_username):
    if ' ' not in some_username:
        return True


def username_is_valid():
    if length_check(username) and symbols_check(username) and redundant_check(username):
        return True


usernames = input().split(', ')

for username in usernames:
    if username_is_valid():
        print(username)