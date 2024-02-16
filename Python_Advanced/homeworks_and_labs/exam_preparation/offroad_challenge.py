from collections import deque

fuel_quantity = [int(x) for x in input().split()]
consumption_indexes = deque(int(x) for x in input().split())
needed_fuel = deque(int(x) for x in input().split())

reached_altitudes = []

for n in range(1, len(fuel_quantity) + 1):
    fuel = fuel_quantity.pop()
    consum_index = consumption_indexes.popleft()

    result = fuel - consum_index
    fuel_needed = needed_fuel.popleft()

    if result < fuel_needed:
        print(f"John did not reach: Altitude {n}")
        print("John failed to reach the top.")
        print(f"Reached altitudes: {', '.join(reached_altitudes)}") if reached_altitudes else print("John didn't reach any altitude.")
        exit()

    reached_altitudes.append(f'Altitude {n}')
    print(f"John has reached: Altitude {n}")

print(f"John has reached all the altitudes and managed to reach the top!")