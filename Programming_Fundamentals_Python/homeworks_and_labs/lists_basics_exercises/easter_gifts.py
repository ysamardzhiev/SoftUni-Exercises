gifts = input().split()

command_line = input()
while command_line != 'No Money':
    commands = command_line.split()
    command = commands[0]
    item = commands[1]
    if command == 'OutOfStock':
        for current_gift in gifts:
            if current_gift in commands:
                gift_index = gifts.index(current_gift)
                gifts[gift_index] = 'None'
    elif command == 'Required':
        index = int(commands[2])
        if 0 <= index < len(gifts):
            gifts[index] = item
    elif command == 'JustInCase':
        gifts[-1] = item
    command_line = input()
for element in gifts:
    if 'None' in gifts:
        gifts.remove('None')
print(' '.join(gifts))