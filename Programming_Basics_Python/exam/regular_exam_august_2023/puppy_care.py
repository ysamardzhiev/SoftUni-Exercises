bought_food_quantity = int(input())

bought_food_quantity_in_grams = bought_food_quantity * 1000

input_line = input()
total_eaten_food = 0
while input_line != 'Adopted':
    eaten_food = int(input_line)
    total_eaten_food += eaten_food

    input_line = input()

diff = abs(total_eaten_food - bought_food_quantity_in_grams)
if total_eaten_food <= bought_food_quantity_in_grams:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')