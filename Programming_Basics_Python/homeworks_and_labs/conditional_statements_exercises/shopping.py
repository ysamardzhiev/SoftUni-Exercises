budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_total = gpu_count * 250
cpu_total = (gpu_total * 0.35) * cpu_count
ram_total = (gpu_total * 0.10) * ram_count
total_budget = gpu_total + cpu_total + ram_total

if gpu_count > cpu_count:
    total_budget = total_budget - (total_budget * 0.15)

diff = abs(budget - total_budget)

if total_budget <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")