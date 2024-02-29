import os

path = os.path.join('files', 'numbers.txt')

file = open(path)

numbers_sum = 0
for num in file:
    numbers_sum += int(num)

print(numbers_sum)
file.close()