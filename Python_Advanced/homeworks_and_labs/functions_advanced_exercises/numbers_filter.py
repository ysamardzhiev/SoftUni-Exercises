def even_odd_filter(**kwargs):
    filtered_nums = {}

    for numbers_type, numbers in kwargs.items():
        if numbers_type == 'odd':
            filtered_nums[numbers_type] = [num for num in numbers if num % 2]
        elif numbers_type == 'even':
            filtered_nums[numbers_type] = [num for num in numbers if num % 2 == 0]

    return dict(sorted(filtered_nums.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
