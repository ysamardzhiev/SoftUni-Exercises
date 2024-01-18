from collections import deque

n = int(input())

numbers = deque()

for _ in range(n):
    query = input().split()
    command = query[0]
    if command == '1':
        numbers.append(int(query[1]))
    elif command == '2':
        if numbers:
            numbers.pop()
    elif command == '3':
        if numbers:
            print(max(numbers))
    elif command == '4':
        if numbers:
            print(min(numbers))
numbers = [str(number) for number in numbers]
numbers.reverse()
print(', '.join(numbers))