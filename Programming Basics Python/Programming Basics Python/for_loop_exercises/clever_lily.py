age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

saved_money = 0
toy_count = 0
stolen_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        saved_money += int(year / 2) * 10
        stolen_money += 1
    else:
        toy_count += 1

money_from_toys = toy_count * price_toy
total_saved_money = saved_money + money_from_toys - stolen_money
diff = abs(total_saved_money - price_washing_machine)

if total_saved_money >= price_washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
