first_set = set(input().split())
second_set = set(input().split())

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'Add':
        number = command.pop()
        while number.isdigit():
            if command[1] == 'First':
                first_set.add(number)
            else:
                second_set.add(number)
            number = command.pop()
    elif command[0] == 'Remove':
        number = command.pop()
        while number.isdigit():
            if command[1] == 'First' and number in first_set:
                first_set.remove(number)
            elif command[1] == 'Second' and number in second_set:
                second_set.remove(number)
            number = command.pop()
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')
print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')