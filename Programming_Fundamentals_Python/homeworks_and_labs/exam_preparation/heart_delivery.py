neighbourhood = [int(s) for s in input().split('@')]

already_had_valentines = []
index = 0

command_line = input()
while command_line != 'Love!':
    commands = command_line.split()
    length = int(commands[1])
    index += length
    if index >= len(neighbourhood):
        index = 0
    if neighbourhood[index] > 0:
        neighbourhood[index] -= 2
    if neighbourhood[index] == 0 and index in already_had_valentines:
        print(f"Place {index} already had Valentine's day.")
    elif neighbourhood[index] == 0:
        print(f"Place {index} has Valentine's day.")
        already_had_valentines.append(index)
    command_line = input()

not_celebrated_houses = [num for num in neighbourhood if num != 0]

print(f"Cupid's last position was {index}.")
if len(not_celebrated_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(not_celebrated_houses)} places.")