vegetables_price = float(input())
fruits_price = float(input())
vegetables_count = int(input())
fruits_count = int(input())

vegetables_total_price = vegetables_price * vegetables_count
fruits_total_price = fruits_price * fruits_count
total_price = (vegetables_total_price + fruits_total_price) / 1.94

print(f'{total_price:.2f}')