elements = [element.lower() for element in input().split()]

elements_dict = {}

for element in elements:
    if element in elements_dict:
        elements_dict[element] += 1
    else:
        elements_dict[element] = 1

for key, value in elements_dict.items():
    if value % 2:
        print(key, end=' ')