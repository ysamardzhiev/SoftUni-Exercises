n = int(input())

numbers = []

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
numbers.reverse()
print(*numbers, sep=', ')