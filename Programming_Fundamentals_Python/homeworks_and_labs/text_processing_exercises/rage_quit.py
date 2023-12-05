string = input()

current_string = ''
rage_message = ''

for index in range(len(string)):
    if string[index].isdigit():
        repetitions = ''
        for i in range(index, len(string)):
            if string[i].isdigit():
                repetitions += string[i]
            else:
                break
        rage_message += current_string.upper() * int(repetitions)
        current_string = ''
    else:
        current_string += string[index]

unique_symbols = len(set(rage_message))
print(f'Unique symbols used: {unique_symbols}')
print(rage_message)