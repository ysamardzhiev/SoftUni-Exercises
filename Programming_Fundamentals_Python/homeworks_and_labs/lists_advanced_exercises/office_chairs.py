def rooms_check(rooms_count: int) -> int:
    free_chairs_counter = 0

    for room in range(1, rooms_count + 1):
        chair_and_visitors_count = input().split()
        chairs = len(chair_and_visitors_count[0])
        visitors = int(chair_and_visitors_count[1])
        free_chairs_counter += chairs - visitors

        if visitors > chairs:
            print(f'{visitors - chairs} more chairs needed in room {room}')
    return free_chairs_counter


number_of_rooms = int(input())
total_free_chairs = rooms_check(number_of_rooms)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')