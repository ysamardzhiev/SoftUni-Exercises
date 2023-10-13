n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command_line = input()

filtered_numbers = []

for current_num in numbers:
    if command_line == 'even':
        if current_num % 2 == 0:
            filtered_numbers.append(current_num)
    elif command_line == 'odd':
        if current_num % 2:
            filtered_numbers.append(current_num)
    elif command_line == 'negative':
        if current_num < 0:
            filtered_numbers.append(current_num)
    elif command_line == 'positive':
        if current_num >= 0:
            filtered_numbers.append(current_num)
print(filtered_numbers)