from collections import deque

dispenser_capacity = int(input())

customers = deque()

command = input()
while command != 'Start':
    name = command
    customers.append(name)
    command = input()

command = input()
while command != 'End':
    if command.isdigit():
        liters = int(command)
        current_customer = customers.popleft()
        if dispenser_capacity >= liters:
            dispenser_capacity -= liters
            print(f'{current_customer} got water')
        else:
            print(f'{current_customer} must wait')
    else:
        command, liters = command.split()
        dispenser_capacity += int(liters)
    command = input()
print(f'{dispenser_capacity} liters left')