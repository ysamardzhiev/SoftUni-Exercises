n = int(input())

guests = set()

for _ in range(n):
    reservation_code = input()
    guests.add(reservation_code)

guest = input()
while guest != 'END':
    if guest in guests:
        guests.remove(guest)
    guest = input()

formatted_set = sorted(guests, key=lambda x: x if x[0].isdigit else x)
print(len(guests))
print('\n'.join(formatted_set))