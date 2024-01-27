from collections import deque

bees = deque(int(num) for num in input().split())
nectar = deque(int(num) for num in input().split())
symbols = deque(input().split())
hive = deque()

while bees and nectar:
    bee_value = bees.popleft()
    nectar_value = nectar.pop()
    if nectar_value >= bee_value:
        symbol = symbols.popleft()
        if symbol == '/' and nectar_value == 0:
            continue
        hive.append(abs(eval(f'{bee_value} {symbol} {nectar_value}')))
    else:
        bees.appendleft(bee_value)
print(f'Total honey made: {sum(hive)}')
if bees:
    print(f'Bees left: {", ".join(str(num) for num in bees)}')
elif nectar:
    print(f'Nectar left: {", ".join(str(num) for num in nectar)}')