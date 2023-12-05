class Party:
    people = []

    def __init__(self):
        pass


command = input()
while command != 'End':
    name = command
    Party.people.append(name)
    command = input()

print(f'Going: {", ".join(Party.people)}')
print(f'Total: {len(Party.people)}')