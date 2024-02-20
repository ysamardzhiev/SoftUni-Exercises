text = input()

try:
    repeat_count = int(input())
    print(text * repeat_count)
except ValueError as ex:
    print('Variable times must be an integer')