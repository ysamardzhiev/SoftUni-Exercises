from collections import deque

clients = deque()

command = input()
while command != 'End':
    if command == 'Paid':
        while clients:
            print(clients.popleft())
    else:
        client = command
        clients.append(client)
    command = input()
print(f'{len(clients)} people remaining.')