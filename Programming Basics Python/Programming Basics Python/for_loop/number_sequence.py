from sys import maxsize
count_numbers = int(input())

max_number = -maxsize
min_number = maxsize

for i in range(count_numbers):
    type_number = int(input())
    if type_number > max_number:
        max_number = type_number

    if type_number < min_number:
        min_number = type_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')