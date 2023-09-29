total_sum = 0

while True:
    data = input()
    if data == 'NoMoreMoney':
        break
    current_money = float(data)
    if current_money > 0:
        total_sum += current_money
        print(f'Increase: {current_money:.2f}')
    elif current_money < 0:
        print('Invalid operation!')
        break

print(f'Total: {total_sum:.2f}')