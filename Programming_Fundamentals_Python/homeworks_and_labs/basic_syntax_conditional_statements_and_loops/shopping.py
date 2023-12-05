budget = int(input())

total_purchase_value = 0

input_line = input()
while input_line != 'End':
    acquired_item = int(input_line)
    total_purchase_value += acquired_item

    if total_purchase_value > budget:
        print("You went in overdraft!")
        break

    input_line = input()
else:
    print("You bought everything needed.")