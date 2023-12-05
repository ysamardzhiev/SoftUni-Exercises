def left_racer(some_numbers: list) -> float:
    total_time = 0
    for index in range(len(some_numbers)):
        if some_numbers[index] == 0:
            total_time *= 0.8
        else:
            total_time += some_numbers[index]
    return total_time


def right_racer(some_numbers: list) -> float:
    total_time = 0
    for index in range(len(some_numbers)):
        if some_numbers[index] == 0:
            total_time *= 0.8
        else:
            total_time += some_numbers[index]
    return total_time


numbers = [int(s) for s in input().split()]

finish_line = len(numbers) // 2
left_racer_timings = numbers[:finish_line]
right_racer_timings = numbers[len(numbers):finish_line:-1]

left_total_time = left_racer(left_racer_timings)
right_total_time = right_racer(right_racer_timings)

if left_total_time < right_total_time:
    print(f'The winner is left with total time: {left_total_time:.1f}')
else:
    print(f'The winner is right with total time: {right_total_time:.1f}')