text = [char for char in input()]

reversed_string = ''

while text:
    reversed_string += text.pop()
print(reversed_string)