from collections import deque

material_boxes = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}

crafted_presents = {}

while material_boxes and magic_levels:
    material_value, magic_level = material_boxes.pop(), magic_levels.popleft()
    if material_value == 0 and magic_level == 0:
        continue
    elif magic_level == 0:
        material_boxes.append(material_value)
        continue
    elif material_value == 0:
        magic_levels.appendleft(magic_level)
        continue
    total_magic_level = material_value * magic_level

    if total_magic_level in presents.keys():
        toy = presents[total_magic_level]
        if toy not in crafted_presents:
            crafted_presents[toy] = 0
        crafted_presents[toy] += 1
    elif total_magic_level < 0:
        total_magic_level = material_value + magic_level
        material_boxes.append(total_magic_level)
    elif total_magic_level > 0:
        material_boxes.append(material_value + 15)

if 'Doll' and 'Wooden train' in crafted_presents or 'Teddy bear' and 'Bicycle' in crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_boxes:
    print(f'Materials left: {", ".join(str(x) for x in material_boxes[::-1])}')
elif magic_levels:
    print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')

for toy, amount in sorted(crafted_presents.items()):
    print(f'{toy}: {amount}')