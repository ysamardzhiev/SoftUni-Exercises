from collections import deque

clients = deque([])

command = input()
while command != 'End':
    if command == 'Paid':
        print('\n'.join(clients))
        clients.clear()
        command = input()
        continue
    client = command
    clients.append(client)
    command = input()
print(f'{len(clients)} people remaining.')