from sys import maxsize
count_numbers = int(input())

total_sum = 0
max_number = -maxsize

for _ in range(count_numbers):
    current_number = int(input())
    total_sum += current_number

    if max_number < current_number:
        max_number = current_number

if total_sum - max_number == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number - (total_sum - max_number))
    print('No')
    print(f'Diff = {diff}')