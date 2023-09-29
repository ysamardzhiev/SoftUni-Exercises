x = float(input())
y = float(input())
h = float(input())

# WALLS

side_wall = x * y
window = 1.5 * 1.5
both_side_walls = 2 * side_wall - 2 * window

back_wall = x * x
door = 1.2 * 2
back_and_front_wall = 2 * back_wall - door

area_walls = both_side_walls + back_and_front_wall
green_paint = area_walls / 3.4

# ROOF

both_rectangles_of_the_roof = 2 * (x * y)
both_triangles = 2 * (x * h / 2)

area_roof = both_rectangles_of_the_roof + both_triangles
red_paint = area_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')