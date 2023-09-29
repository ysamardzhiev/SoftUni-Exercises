cake_length = int(input())
cake_width = int(input())
pieces_count = cake_width * cake_length

total_sum = pieces_count

input_line = input()
while input_line != 'STOP':
    one_piece = int(input_line)
    total_sum -= one_piece

    if total_sum <= 0:
        break

    input_line = input()

if input_line == 'STOP':
    print(f'{total_sum} pieces are left.')
else:
    diff = abs(total_sum)
    print(f'No more cake left! You need {diff} pieces more.')