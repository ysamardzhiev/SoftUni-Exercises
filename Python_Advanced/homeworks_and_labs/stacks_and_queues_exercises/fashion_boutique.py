clothes = [int(value) for value in input().split()]
rack_capacity = int(input())

clothes_sum = 0
total_racks = 1

while clothes:
    current_clothes = clothes.pop()
    clothes_sum += current_clothes
    if clothes_sum == rack_capacity:
        if clothes:
            total_racks += 1
            clothes_sum = 0
    elif clothes_sum > rack_capacity:
        clothes.append(current_clothes)
        clothes_sum = 0
        total_racks += 1
print(total_racks)