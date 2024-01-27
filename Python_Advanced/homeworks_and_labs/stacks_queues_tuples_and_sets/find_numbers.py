first_set = set(int(num) for num in input().split())
second_set = set(int(num) for num in input().split())

for _ in range(int(input())):
    first_command, second_command, *numbers = input().split()
    if first_command == 'Add':
        while numbers:
            number = int(numbers.pop())
            if second_command == 'First':
                first_set.add(number)
            else:
                second_set.add(number)
    elif first_command == 'Remove':
        while numbers:
            number = int(numbers.pop())
            if second_command == 'First':
                first_set.discard(number)
            else:
                second_set.discard(number)
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')
print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')