n = int(input())

longest_intersection = set()

for _ in range(n):
    ranges = input().split('-')
    first_start, first_end = [int(num) for num in ranges[0].split(',')]
    second_start, second_end = [int(num) for num in ranges[1].split(',')]

    first_set = {num for num in range(first_start, first_end+1)}
    second_set = {num for num in range(second_start, second_end+1)}

    intersection_set = first_set.intersection(second_set)
    if len(longest_intersection) < len(intersection_set):
        longest_intersection = intersection_set
print(f'Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}')