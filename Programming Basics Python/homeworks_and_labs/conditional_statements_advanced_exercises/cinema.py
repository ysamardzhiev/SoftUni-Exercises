type_project = input()
row_count = int(input())
column_count = int(input())
price = 0

if type_project == 'Premiere':
    price = 12
elif type_project == 'Normal':
    price = 7.50
elif type_project == 'Discount':
    price = 5

cinema_hall = row_count * column_count
total_price = price * cinema_hall
print(f'{total_price:.2f} leva')