phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        break
    name, phone_number = entry.split('-')
    phonebook[name] = phone_number

n = int(entry)

for contact in range(n):
    name = input()
    if name in phonebook.keys():
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')