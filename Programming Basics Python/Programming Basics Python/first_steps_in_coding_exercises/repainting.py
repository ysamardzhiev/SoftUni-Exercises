nylon = int(input())
paint = int(input())
thinner = int(input())
time = int(input())

sum_nylon = (nylon + 2) * 1.50
sum_paint = (paint + 1.1) * 14.5
sum_thinner = thinner * 5
sum_bags = 0.4

total_sum_materials = sum_nylon + sum_paint + sum_thinner + sum_bags
sum_workers = (total_sum_materials * 30 / 100) * time
final_sum = total_sum_materials + sum_workers

print(final_sum)
