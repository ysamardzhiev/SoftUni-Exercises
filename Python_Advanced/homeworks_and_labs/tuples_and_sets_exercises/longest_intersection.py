n = int(input())

longest_intersection = set()

for _ in range(n):
    first_data, second_data = [el.split(',') for el in input().split('-')]

    first_set = set(range(int(first_data[0]), int(first_data[1])+1))
    second_set = set(range(int(second_data[0]), int(second_data[1])+1))

    intersection_set = first_set.intersection(second_set)
    if len(longest_intersection) < len(intersection_set):
        longest_intersection = intersection_set
print(f'Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}')