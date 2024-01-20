from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    while bottles:
        bottle = bottles.pop()
        cup -= bottle
        if cup <= 0:
            wasted_water += abs(cup)
            break
if cups:
    print('Cups:', *cups)
else:
    print('Bottles:', *bottles)
print(f'Wasted litters of water: {wasted_water}')