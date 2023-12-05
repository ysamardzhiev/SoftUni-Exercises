houses = [int(s) for s in input().split('@')]

index = 0

command_line = input()
while command_line != 'Love!':
    commands = command_line.split()
    length = int(commands[1])
    index += length
    if index >= len(houses):
        index = 0
    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")
    command_line = input()

not_celebrated_houses = [num for num in houses if num != 0]

print(f"Cupid's last position was {index}.")
if len(not_celebrated_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(not_celebrated_houses)} places.")