from collections import deque

n = int(input())

stack = deque()

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        stack.append(int(query[1]))
    elif query[0] == '2':
        if stack:
            stack.pop()
    elif query[0] == '3':
        if stack:
            print(max(stack))
    elif query[0] == '4':
        if stack:
            print(min(stack))
stack = [str(number) for number in stack]
stack.reverse()
print(', '.join(stack))