number_of_rooms = int(input())

total_free_chairs = 0
total_needed_chairs = 0
for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs_count = chairs_and_visitors[0].count('X')
    visitors_count = int(chairs_and_visitors[1])
    if chairs_count < visitors_count:
        needed_chairs = visitors_count - chairs_count
        total_needed_chairs += needed_chairs
        print(f'{needed_chairs} more chairs needed in room {room}')
    else:
        total_free_chairs += chairs_count - visitors_count
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")