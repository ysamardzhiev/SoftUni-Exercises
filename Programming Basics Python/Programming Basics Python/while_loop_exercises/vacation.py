budget_for_vacation = float(input())
starting_money = float(input())

total_sum = starting_money
days_counter = 0
spend_counter = 0

while total_sum < budget_for_vacation:
    if spend_counter == 5:
        break
    spend_or_save = input()
    money_to_spend_or_save = float(input())

    days_counter += 1

    if spend_or_save == 'spend':
        spend_counter += 1
        total_sum -= money_to_spend_or_save
        if total_sum < 0:
            total_sum = 0
    else:
        total_sum += money_to_spend_or_save
        spend_counter = 0

if spend_counter == 5:
    print(f"You can't save the money.\n{days_counter}")
else:
    print(f'You saved the money for {days_counter} days.')