wagons_count = int(input())

train_wagons = [0 for num in range(wagons_count)]

command = input()
while command != 'End':
    commands = command.split()

    if commands[0] == 'add':
        people_count = int(commands[1])
        train_wagons[-1] += people_count
    elif commands[0] == 'insert':
        index = int(commands[1])
        people_count = int(commands[2])
        train_wagons[index] += people_count
    elif commands[0] == 'leave':
        index = int(commands[1])
        people_count = int(commands[2])
        train_wagons[index] -= people_count
    command = input()
print(train_wagons)