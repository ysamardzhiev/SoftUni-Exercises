import string

strings = [string.strip() for string in input().split()]

total_sum = 0

for text in strings:
    current_number = int(text[1:len(text) - 1])
    if text[0].islower():
        letter_position = string.ascii_lowercase.index(text[0]) + 1
        total_sum += current_number * letter_position
    else:
        letter_position = string.ascii_uppercase.index(text[0]) + 1
        total_sum += current_number / letter_position

    if text[-1].islower():
        letter_position = string.ascii_lowercase.index(text[-1]) + 1
        total_sum += letter_position
    else:
        letter_position = string.ascii_uppercase.index(text[-1]) + 1
        total_sum -= letter_position
print(f'{total_sum:.2f}')