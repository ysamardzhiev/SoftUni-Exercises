from collections import deque

color_substrings = deque(input().split())
searched_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

formed_colors = []

while color_substrings:
    if len(color_substrings) == 1:
        color = color_substrings.pop()
        if color in searched_colors:
            formed_colors.append(color)
    else:
        first_substring, second_substring = color_substrings.popleft(), color_substrings.pop()

        if first_substring + second_substring in searched_colors:
            formed_colors.append(first_substring + second_substring)
        elif second_substring + first_substring in searched_colors:
            formed_colors.append(second_substring + first_substring)
        else:
            if len(first_substring) > 1:
                color_substrings.insert(len(color_substrings) // 2, first_substring[:len(first_substring) - 1])
            if len(second_substring) > 1:
                color_substrings.insert(len(color_substrings) // 2, second_substring[:len(second_substring) - 1])
for color in formed_colors:
    if color == 'orange' and not {'red', 'yellow'}.issubset(formed_colors):
        formed_colors.remove(color)
    elif color == 'purple' and not {'red', 'blue'}.issubset(formed_colors):
        formed_colors.remove(color)
    elif color == 'green' and not {'yellow', 'blue'}.issubset(formed_colors):
        formed_colors.remove(color)
print(formed_colors)