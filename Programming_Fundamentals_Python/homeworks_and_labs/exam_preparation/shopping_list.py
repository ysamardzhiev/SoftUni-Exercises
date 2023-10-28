groceries = input().split('!')

command = input()
while command != "Go Shopping!":
    commands = command.split()
    type_of_command = commands[0]
    item = commands[1]
    if type_of_command == 'Urgent':
        if item not in groceries:
            groceries.insert(0, item)
    elif type_of_command == 'Unnecessary':
        if item in groceries:
            groceries.remove(item)
    elif type_of_command == 'Correct':
        new_item = commands[2]
        if item in groceries:
            index = groceries.index(item)
            groceries[index] = new_item
    elif type_of_command == 'Rearrange':
        if item in groceries:
            groceries.append(item)
            groceries.remove(item)
    command = input()
print(', '.join(groceries))