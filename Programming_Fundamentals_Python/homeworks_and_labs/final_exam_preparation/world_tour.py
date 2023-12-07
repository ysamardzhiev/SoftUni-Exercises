stops = input()

command = input()
while command != 'Travel':
    commands = command.split(':')
    if commands[0] == 'Add Stop':
        index, string = int(commands[1]), commands[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index::]
        print(stops)
    elif commands[0] == 'Remove Stop':
        start_index, end_index = int(commands[1]), int(commands[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1::]
        print(stops)
    elif commands[0] == 'Switch':
        old_string, new_string = commands[1], commands[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")