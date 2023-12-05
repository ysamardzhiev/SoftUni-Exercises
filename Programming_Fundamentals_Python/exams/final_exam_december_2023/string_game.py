string = input()

command = input()
while command != 'Done':
    commands = command.split()
    action = commands[0]
    if action == 'Change':
        char, replacement = commands[1], commands[2]
        string = string.replace(char, replacement)
        print(string)
    elif action == 'Includes':
        substring = commands[1]
        if substring in string:
            print('True')
        else:
            print('False')
    elif action == 'End':
        substring = commands[1]
        if substring.endswith(substring):
            print('True')
        else:
            print('False')
    elif action == 'Uppercase':
        string = string.upper()
        print(string)
    elif action == 'FindIndex':
        char = commands[1]
        char_index = string.index(char)
        print(char_index)
    elif action == 'Cut':
        start_index, count = int(commands[1]), int(commands[2])
        cut_chars = ''
        for _ in range(count):
            cut_chars += string[start_index]
            start_index += 1
        print(cut_chars)
    command = input()