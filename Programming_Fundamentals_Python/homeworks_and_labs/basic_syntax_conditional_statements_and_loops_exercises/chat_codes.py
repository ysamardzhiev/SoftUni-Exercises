n = int(input())

for _ in range(n):
    current_number = int(input())

    if current_number == 88:
        print('Hello')
    elif current_number == 86:
        print('How are you?')
    elif current_number < 86:
        print('GREAT!')
    else:
        print('Bye.')