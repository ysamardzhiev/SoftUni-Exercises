parking_lot = {}

n = int(input())

for _ in range(n):
    commands = input().split()
    command, username = commands[0], commands[1]
    if command == 'register':
        license_plate = commands[2]
        if username not in parking_lot.keys():
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == 'unregister':
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")