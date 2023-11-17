materials = {'shards': 0, 'fragments': 0, 'motes': 0}
item_value = 250
obtained_item = ''
item_already_obtained = False

while not item_already_obtained:
    line_of_materials = input().split()
    for i in range(0, len(line_of_materials), 2):
        quantity = int(line_of_materials[i])
        material = line_of_materials[i+1].lower()
        if material not in materials.keys():
            materials[material] = 0
        materials[material] += quantity
        if materials['shards'] >= item_value:
            obtained_item = 'Shadowmourne'
            item_already_obtained = True
            materials[material] -= item_value
        elif materials['fragments'] >= item_value:
            obtained_item = 'Valanyr'
            item_already_obtained = True
            materials[material] -= item_value
        elif materials['motes'] >= item_value:
            obtained_item = 'Dragonwrath'
            item_already_obtained = True
            materials[material] -= item_value
        if item_already_obtained:
            break

print(f'{obtained_item} obtained!')
for material, quantity in materials.items():
    print(f'{material}: {quantity}')