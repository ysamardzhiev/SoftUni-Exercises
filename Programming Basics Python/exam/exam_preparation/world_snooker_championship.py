competition_stage = input()
ticket_type = input()
ticket_count = int(input())
picture_with_cup = input()

tickets_price = 0

if competition_stage == 'Final':
    if ticket_type == 'Standard':
        tickets_price = 110.10
    elif ticket_type == 'Premium':
        tickets_price = 160.66
    elif ticket_type == 'VIP':
        tickets_price = 400
elif competition_stage == 'Semi final':
    if ticket_type == 'Standard':
        tickets_price = 75.88
    elif ticket_type == 'Premium':
        tickets_price = 125.22
    elif ticket_type == 'VIP':
        tickets_price = 300.40
elif competition_stage == 'Quarter final':
    if ticket_type == 'Standard':
        tickets_price = 55.50
    elif ticket_type == 'Premium':
        tickets_price = 105.20
    elif ticket_type == 'VIP':
        tickets_price = 118.90

total_ticket_price = tickets_price * ticket_count

if total_ticket_price >= 4000:
    total_ticket_price -= total_ticket_price * 0.25
    picture_with_cup = 'N'
elif total_ticket_price > 2500:
    total_ticket_price -= total_ticket_price * 0.10

if picture_with_cup == 'Y':
    total_ticket_price += (ticket_count * 40)
else:
    total_ticket_price = total_ticket_price

print(f'{total_ticket_price:.2f}')