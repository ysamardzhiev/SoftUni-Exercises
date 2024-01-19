from collections import deque

number_of_petrol_pumps = int(input())

circle_road = deque()

for _ in range(number_of_petrol_pumps):
    circle_road.append(input().split())

circle_road_copy = circle_road.copy()
tank_capacity = 0
index = 0

while circle_road_copy:
    data = circle_road_copy.popleft()
    petrol, distance = [int(x) for x in data]
    tank_capacity += petrol
    if tank_capacity >= distance:
        tank_capacity -= distance
    else:
        circle_road.rotate(-1)
        circle_road_copy = circle_road.copy()
        tank_capacity = 0
        index += 1
print(index)