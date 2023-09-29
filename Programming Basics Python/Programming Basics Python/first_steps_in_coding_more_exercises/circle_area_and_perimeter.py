from math import pi

radius = float(input())
face_area = pi * (radius ** 2)
parameter_area = 2 * pi * radius

print(f'{face_area:.2f}')
print(f'{parameter_area:.2f}')