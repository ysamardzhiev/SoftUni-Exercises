budget = float(input())
tickets_type = input()
people_count = int(input())

price = 0

normal_ticket_price = 249.99 * people_count
vip_ticket_price = 499.99 * people_count

if 1 <= people_count <= 4:
    price = budget * 0.25
elif 5 <= people_count <= 9:
    price = budget * 0.4
elif 10 <= people_count <= 24:
    price = budget * 0.5
elif 25 <= people_count <= 49:
    price = budget * 0.6
elif people_count >= 50:
    price = budget * 0.75

diff_normal_ticket = abs(price - normal_ticket_price)
diff_vip_ticket = abs(price - vip_ticket_price)

if tickets_type == 'Normal':
    if price >= diff_normal_ticket:
        print(f"Yes! You have {diff_normal_ticket:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff_normal_ticket:.2f} leva.")
elif tickets_type == 'VIP':
    if price >= vip_ticket_price:
        print(f"Yes! You have {diff_vip_ticket:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff_vip_ticket:.2f} leva.")