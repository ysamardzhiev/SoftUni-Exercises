from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())
snake_copy = snake.copy()

for row_index in range(rows):
    row = [' ' for _ in range(cols)]
    for col_index in range(cols):
        if not snake_copy:
            snake_copy = snake.copy()
        current_symbol = snake_copy.popleft()
        if row_index % 2 == 0:
            row[col_index] = current_symbol
        else:
            row[cols - col_index - 1] = current_symbol
    print(*row, sep='')