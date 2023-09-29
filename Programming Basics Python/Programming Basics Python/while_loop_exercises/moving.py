width = int(input())
length = int(input())
height = int(input())

total_free_space = width * length * height
total_sum_cubic_meters = 0
no_free_space = False

input_line = input()
while input_line != 'Done':
    cubic_meters = int(input_line)
    total_sum_cubic_meters += cubic_meters

    if total_sum_cubic_meters >= total_free_space:
        no_free_space = True
        break

    input_line = input()

diff = abs(total_free_space - total_sum_cubic_meters)
if no_free_space:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')
