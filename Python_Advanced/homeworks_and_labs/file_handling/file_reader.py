file_name = 'numbers.txt'

file = open(file_name)

numbers_sum = 0
for num in file:
    numbers_sum += int(num)

print(numbers_sum)
