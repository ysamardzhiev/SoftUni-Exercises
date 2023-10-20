def chars_between(char1: str, char2: str) -> str:
    some_string = ''
    for character in range(ord(char1) + 1, ord(char2)):
        some_string += f'{chr(character)} '
    return some_string


first_char = input()
second_char = input()
result = chars_between(first_char, second_char)
print(result)