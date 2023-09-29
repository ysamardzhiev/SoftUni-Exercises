from sys import maxsize

max_number = -maxsize

while True:
    data = input()
    if data == 'Stop':
        break
    number = int(data)
    if number > max_number:
        max_number = number
print(max_number)

# data = input()
# while data != 'Stop':
#     number = int(data)
#     if number > max_number:
#         max_number = number
#     data = input()
#
# print(max_number)
