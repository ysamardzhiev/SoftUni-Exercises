number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = [int(mileage), int(fuel)]

command = input()
while command != 'Stop':
    commands = command.split(' : ')
    if commands[0] == 'Drive':
        car, distance, fuel = commands[1], int(commands[2]), int(commands[3])
        if fuel > cars[car][1]:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    elif commands[0] == 'Refuel':
        car, fuel = commands[1], int(commands[2])
        fuel_to_add = min(fuel, 75 - cars[car][1])
        cars[car][1] += fuel_to_add
        print(f"{car} refueled with {fuel_to_add} liters")
    else:
        car, kilometers = commands[1], int(commands[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
            command = input()
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

for car in cars.keys():
    mileage, fuel = cars[car][0], cars[car][1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")