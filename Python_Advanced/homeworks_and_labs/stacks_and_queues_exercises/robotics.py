from collections import deque
from datetime import datetime, timedelta

robots = {}
products = deque()

for robot in input().split(';'):
    name, time_needed = robot.split('-')
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), '%H:%M:%S')

command = input()
while command != 'End':
    product = command
    products.append(product)
    command = input()

while products:
    factory_time += timedelta(seconds=1)
    product = products.popleft()

    free_robots = []

    for current_robot, value in robots.items():
        if value[1] == value[0]:
            value[1] = 0
        if value[1] == 0:
            if free_robots:
                continue
            free_robots.append(current_robot)
        value[1] += 1
    if free_robots:
        print(f'{free_robots.pop()} - {product} [{factory_time.time()}]')
    else:
        products.append(product)