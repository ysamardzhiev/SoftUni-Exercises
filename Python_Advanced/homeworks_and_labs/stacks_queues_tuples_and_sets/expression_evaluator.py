from collections import deque

expression = deque(input().split())
numbers = deque()

while expression:
    symbol = expression.popleft()
    if not symbol.isdigit() and len(symbol) == 1:
        current_num = numbers.popleft()
        while numbers:
            if symbol == '+':
                current_num += numbers.popleft()
            elif symbol == '-':
                current_num -= numbers.popleft()
            elif symbol == '*':
                current_num *= numbers.popleft()
            elif symbol == '/':
                current_num //= numbers.popleft()
        numbers.append(current_num)
    else:
        numbers.append(int(symbol))
print(*numbers)