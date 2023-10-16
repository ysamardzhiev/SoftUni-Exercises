money_as_str = input().split(', ')
beggars_count = int(input())

money_as_int = []

for current_money in money_as_str:
    money_as_int.append(int(current_money))

beggars_money_sum = []
start_index = 0

for current_beggar in range(beggars_count):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_int), beggars_count):
        current_beggar_sum += money_as_int[index]
    beggars_money_sum.append(current_beggar_sum)
    start_index += 1
print(beggars_money_sum)
