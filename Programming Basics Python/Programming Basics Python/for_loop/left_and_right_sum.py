count_numbers = int(input())

left_sum = 0
right_sum = 0

for _ in range(count_numbers):
    left_numbers = int(input())
    left_sum += left_numbers
for _ in range(count_numbers):
    right_numbers = int(input())
    right_sum += right_numbers

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')