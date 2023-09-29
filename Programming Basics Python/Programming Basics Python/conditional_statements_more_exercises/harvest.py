from math import ceil, floor

vineyard_area = int(input())
grapes_count = float(input())
wine_needed = int(input())
workers_count = int(input())

total_grapes = vineyard_area * grapes_count
wine = (total_grapes / 2.5) * 0.4
diff = abs(wine - wine_needed)
diff_rounded = ceil(diff)
wine_per_worker = diff / workers_count

if wine >= wine_needed:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{diff_rounded} liters left -> {ceil(wine_per_worker)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
