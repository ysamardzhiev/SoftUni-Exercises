quantity = int(input())
days = int(input())

total_price = 0
total_points = 0

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_price += ornament_set_price * quantity
        total_points += ornament_set_points
    if current_day % 3 == 0 and current_day % 5 == 0:
        total_points += 30
    if current_day % 3 == 0:
        total_price += (tree_skirt_price + tree_garland_price) * quantity
        total_points += tree_skirt_points + tree_garland_points
    if current_day % 5 == 0:
        total_price += tree_lights_price * quantity
        total_points += tree_lights_points
    if current_day % 10 == 0:
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price
        total_points -= 20

if days % 10 == 0:
    total_points -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {total_points}")
