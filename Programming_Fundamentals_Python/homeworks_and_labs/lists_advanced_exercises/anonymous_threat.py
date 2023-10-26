strings = input().split()

command_line = input()
while command_line != '3:1':
    commands = command_line.split()
    type_of_command = commands[0]
    if type_of_command == 'merge':
        start_index = int(commands[1])
        end_index = int(commands[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(strings) - 1:
            end_index = len(strings) - 1
        merged_elements = ''.join(strings[start_index:end_index + 1])
        strings[start_index:end_index + 1] = [merged_elements]
    elif type_of_command == 'divide':
        index = int(commands[1])
        partitions = int(commands[2])
        element = strings[index]
        partitions_length = len(element) // partitions
        divided_partition = []
        for element_index in range(partitions):
            if element_index != partitions - 1:
                divided_partition.append(element[element_index * partitions_length: (element_index + 1) * partitions_length])
            else:
                divided_partition.append(element[element_index * partitions_length:])
        strings[index:index + 1] = divided_partition
    command_line = input()

print(' '.join(strings))