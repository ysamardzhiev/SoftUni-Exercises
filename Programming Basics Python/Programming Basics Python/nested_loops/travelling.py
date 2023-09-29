total_savings = 0

destination = input()
min_budget = float(input())
while destination != 'End':
    while total_savings < min_budget:
        savings = float(input())
        total_savings += savings
    else:
        print(f'Going to {destination}!')

    destination = input()
    total_savings = 0
    if destination != 'End':
        min_budget = float(input())
