from math import ceil

price_per_gpu = int(input())
price_per_cable = int(input())
price_for_electricity_per_day = float(input())
winnings_per_gpu_for_day = float(input())

total_price_gpu = price_per_gpu * 13
total_price_cable = price_per_cable * 13
total_money_spent = total_price_gpu + total_price_cable + 1000

winnings_per_gpu_for_day = winnings_per_gpu_for_day - price_for_electricity_per_day
total_price_per_day_gpu = 13 * winnings_per_gpu_for_day
days_to_payback = total_money_spent / total_price_per_day_gpu

print(total_money_spent)
print(ceil(days_to_payback))