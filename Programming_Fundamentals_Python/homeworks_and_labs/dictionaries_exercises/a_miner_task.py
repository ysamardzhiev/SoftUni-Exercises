resources = {}

current_line = 0
last_added_resource = ''

command = input()
while command != 'stop':
    current_line += 1
    if current_line % 2:
        resource = command
        if resource not in resources.keys():
            resources[resource] = 0
        last_added_resource = resource
    else:
        quantity = command
        resources[last_added_resource] += int(quantity)
    command = input()

for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')