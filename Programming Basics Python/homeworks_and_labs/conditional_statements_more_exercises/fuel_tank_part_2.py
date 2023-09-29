type_fuel = input()
fuel_quantity = float(input())
club_card = input()
discount_gasoline = 2.22 - 0.18
discount_diesel = 2.33 - 0.12
discount_gas = 0.93 - 0.08
total_gasoline_price = discount_gasoline * fuel_quantity
total_diesel_price = discount_diesel * fuel_quantity
total_gas_price = discount_gas * fuel_quantity

price = 0

if club_card == 'Yes':
    if type_fuel == 'Gasoline':
        if 20 <= fuel_quantity <= 25:
            price = total_gasoline_price - (total_gasoline_price * 0.08)
        elif fuel_quantity > 25:
            price = total_gasoline_price - (total_gasoline_price * 0.10)
        else:
            price = total_gasoline_price
    if type_fuel == 'Diesel':
        if 20 <= fuel_quantity <= 25:
            price = total_diesel_price - (total_diesel_price * 0.08)
        elif fuel_quantity > 25:
            price = total_diesel_price - (total_diesel_price * 0.10)
        else:
            price = total_diesel_price
    if type_fuel == 'Gas':
        if 20 <= fuel_quantity <= 25:
            price = total_gas_price - (total_gas_price * 0.08)
        elif fuel_quantity > 25:
            price = total_gas_price - (total_gas_price * 0.10)
        else:
            price = total_gas_price
elif club_card == 'No':
    if type_fuel == 'Gasoline':
        if 20 <= fuel_quantity <= 25:
            price = (2.22 * fuel_quantity) - (2.22 * fuel_quantity * 0.08)
        elif fuel_quantity > 25:
            price = (2.22 * fuel_quantity) - (2.22 * fuel_quantity * 0.10)
        else:
            price = 2.22 * fuel_quantity
    if type_fuel == 'Diesel':
        if 20 <= fuel_quantity <= 25:
            price = (2.33 * fuel_quantity) - (2.33 * fuel_quantity * 0.08)
        elif fuel_quantity > 25:
            price = (2.33 * fuel_quantity) - (2.33 * fuel_quantity * 0.10)
        else:
            price = 2.33 * fuel_quantity
    if type_fuel == 'Gas':
        if 20 <= fuel_quantity <= 25:
            price = (0.93 * fuel_quantity) - (0.93 * fuel_quantity * 0.08)
        elif fuel_quantity > 25:
            price = (0.93 * fuel_quantity) - (0.93 * fuel_quantity * 0.10)
        else:
            price = 0.93 * fuel_quantity

print(f'{price:.2f} lv.')
