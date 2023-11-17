materials = {'shards': 0, 'fragments': 0, 'motes': 0}
win_indicator = 250
obtained_item = ''
item_already_obtained = False

while True:
    line_of_materials = input().split()
    for i in range(0, len(line_of_materials), 2):
        quantity = int(line_of_materials[i])
        material = line_of_materials[i+1].lower()
        if material not in materials.keys():
            materials[material] = 0
        materials[material] += quantity
        if materials['shards'] >= win_indicator or materials['fragments'] >= win_indicator or materials['motes'] >= win_indicator:
            if materials['shards'] >= win_indicator:
                obtained_item = 'Shadowmourne'
            elif materials['fragments'] >= win_indicator:
                obtained_item = 'Valanyr'
            elif materials['motes'] >= win_indicator:
                obtained_item = 'Dragonwrath'
            materials[material] -= win_indicator
            item_already_obtained = True
            break
    if item_already_obtained:
        break

print(f'{obtained_item} obtained!')
for material, quantity in materials.items():
    print(f'{material}: {quantity}')