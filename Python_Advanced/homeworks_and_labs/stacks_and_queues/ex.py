from collections import deque

customers = deque()

command = input()
while command != 'End':
    if command == 'Paid':
        print('\n'.join(customers))
        customers.clear()
    else:
        customer = command
        customers.append(customer)
    command = input()
print(f'{len(customers)} people remaining.')