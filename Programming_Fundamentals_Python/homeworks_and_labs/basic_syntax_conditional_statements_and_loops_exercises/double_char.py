input_line = input()

while input_line != 'End':
    current_string = input_line

    if current_string == 'SoftUni':
        input_line = input()
        continue

    for char in current_string:
        print(f"{char}{char}", end='')
    print()

    input_line = input()
