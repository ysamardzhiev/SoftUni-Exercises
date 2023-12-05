events = input().split('|')

total_energy = 100
total_coins = 100
factory_is_closed = False

for current_event in events:
    type_of_event, event_value = current_event.split('-')
    event_value = int(event_value)
    if type_of_event == 'rest':
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')
    elif type_of_event == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_closed = True
            break
if not factory_is_closed:
    print(f"Day completed!\nCoins: {total_coins}\nEnergy: {total_energy}")
