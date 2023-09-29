floors_count = int(input())
rooms_count = int(input())

for floor in range(floors_count, 0, -1):
    for room in range(rooms_count):
        if floor == floors_count:
            print(f'L{floor}{room}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{room}', end=' ')
        else:
            print(f'A{floor}{room}', end=' ')
    print()

# number_of_floors = int(input())
# number_of_rooms = int(input())
#
# for floor in reversed(range(1, number_of_floors + 1)):
#     if floor % 2:
#         room_type = 'A'
#     else:
#         room_type = 'O'
#
#     if floor == number_of_floors:
#         room_type = 'L'
#
#     for room in range(number_of_rooms):
#         print(f'{room_type}{floor}{room}', end=' ')
#     print()