people_in_the_circle = input().split()
k = int(input())

order_of_executions = []
index = 0
counter = 0

while people_in_the_circle:
    counter += 1
    if counter % k == 0:
        order_of_executions.append(people_in_the_circle[index])
        people_in_the_circle.pop(index)
    else:
        index += 1

    if index >= len(people_in_the_circle):
        index = 0
result = ','.join(order_of_executions)
print(1 * '[' + result + 1 * ']')