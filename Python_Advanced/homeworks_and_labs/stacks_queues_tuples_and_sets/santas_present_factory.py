from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}

crafted_presents = {}

while materials and magic_levels:
    material_value, magic_level = materials.pop(), magic_levels.popleft()

    if not material_value and not magic_level:
        continue
    elif not magic_level:
        materials.append(material_value)
        continue
    elif not material_value:
        magic_levels.appendleft(magic_level)
        continue

    total_magic_level = material_value * magic_level

    if total_magic_level in presents.keys():
        toy = presents[total_magic_level]
        if toy not in crafted_presents.keys():
            crafted_presents[toy] = 0
        crafted_presents[toy] += 1
    elif total_magic_level < 0:
        materials.append(material_value + magic_level)
    elif total_magic_level > 0:
        materials.append(material_value + 15)

if {'Doll', 'Wooden train'}.issubset(crafted_presents) or {'Teddy bear', 'Bicycle'}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials[::-1])}')
if magic_levels:
    print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')

for toy, amount in sorted(crafted_presents.items()):
    print(f'{toy}: {amount}')