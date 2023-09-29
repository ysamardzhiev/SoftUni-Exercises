days_stay = int(input())
type_room = input()
rating = input()

price = 0
nights_stay = days_stay - 1

if type_room == 'room for one person':
    price = nights_stay * 18
elif type_room == 'apartment':
    if days_stay < 10:
        price = (nights_stay * 25) * 0.7
    if 10 <= days_stay <= 15:
        price = (nights_stay * 25) * 0.65
    if days_stay > 15:
        price = (nights_stay * 25) * 0.5
elif type_room == 'president apartment':
    if days_stay < 10:
        price = (nights_stay * 35) * 0.9
    if 10 <= days_stay <= 15:
        price = (nights_stay * 35) * 0.85
    if days_stay > 15:
        price = (nights_stay * 35) * 0.8

if rating == 'positive':
    price = price * (1 + 0.25)
elif rating == 'negative':
    price = price * 0.9

print(f'{price:.2f}')