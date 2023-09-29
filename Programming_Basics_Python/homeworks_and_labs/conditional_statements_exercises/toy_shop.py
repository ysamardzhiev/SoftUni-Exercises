price_vacation = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_plushy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_puzzles = number_of_puzzles * 2.60
total_dolls = number_of_dolls * 3
total_plushy_bears = number_of_plushy_bears * 4.10
total_minions = number_of_minions * 8.20
total_trucks = number_of_trucks * 2
total_toys = number_of_puzzles + number_of_dolls + number_of_plushy_bears + number_of_minions + number_of_trucks

total_price = total_puzzles + total_dolls + total_plushy_bears + total_minions + total_trucks

if total_toys >= 50:
    total_price = total_price - (total_price * 0.25)

total_price = total_price - (total_price * 0.10)

if total_price >= price_vacation:
    print(f'Yes! {total_price - price_vacation:.2f} lv left.')
else:
    print(f'Not enough money! {price_vacation - total_price:.2f} lv needed.')
