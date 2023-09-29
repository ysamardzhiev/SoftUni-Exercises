from sys import maxsize

min_number = maxsize

while True:
    data = input()
    if data == 'Stop':
        break
    number = int(data)
    if number < min_number:
        min_number = number
print(min_number)