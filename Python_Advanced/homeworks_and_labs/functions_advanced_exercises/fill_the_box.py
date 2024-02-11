from collections import deque


def fill_the_box(height, length, width, *args):
    elements = deque(args)
    box_size = height * length * width

    total_cubes = 0

    while elements:
        current_element = elements.popleft()
        if current_element == 'Finish':
            break

        total_cubes += current_element

    if total_cubes >= box_size:
        return f'No more free space! You have {total_cubes - box_size} more cubes.'
    return f'There is free space in the box. You could put {box_size - total_cubes} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))