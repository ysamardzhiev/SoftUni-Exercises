factor = int(input())
count = int(input())

numbers = []
for multiplier in range(1, count + 1):
    current_number = factor * multiplier
    numbers.append(current_number)
print(numbers)

# SECOND OPTION

# factor = int(input())
# count = int(input())
#
# numbers = []
# sum_numbers = 0
# for _ in range(count):
#     sum_numbers += factor
#     numbers.append(sum_numbers)
# print(numbers)