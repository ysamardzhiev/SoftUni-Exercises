from collections import deque

color_substrings = deque(input().split())
searched_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

formed_colors = []

while color_substrings:
    first_substring = color_substrings.popleft()
    second_substring = color_substrings.pop() if color_substrings else ''

    for color in (first_substring + second_substring, second_substring + first_substring):
        if color in searched_colors:
            formed_colors.append(color)
            break
    else:
        for element in (first_substring[:-1], second_substring[:-1]):
            if element:
                color_substrings.insert(len(color_substrings) // 2, element)

for color in set(formed_colors).intersection({'orange', 'purple', 'green'}):
    if color == 'orange' and not {'red', 'yellow'}.issubset(formed_colors):
        formed_colors.remove(color)
    elif color == 'purple' and not {'red', 'blue'}.issubset(formed_colors):
        formed_colors.remove(color)
    elif color == 'green' and not {'yellow', 'blue'}.issubset(formed_colors):
        formed_colors.remove(color)
print(formed_colors)