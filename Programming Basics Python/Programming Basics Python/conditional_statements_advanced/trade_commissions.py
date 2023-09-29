city = input()
sales = float(input())
percent = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        percent = 5 / 100
    elif 500 < sales <= 1000:
        percent = 7 / 100
    elif 1000 < sales <= 10000:
        percent = 8 / 100
    elif sales > 10000:
        percent = 12 / 100
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sales <= 500:
        percent = 4.5 / 100
    elif 500 < sales <= 1000:
        percent = 7.5 / 100
    elif 1000 < sales <= 10000:
        percent = 10 / 100
    elif sales > 10000:
        percent = 13 / 100
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        percent = 5.5 / 100
    elif 500 < sales <= 1000:
        percent = 8 / 100
    elif 1000 < sales <= 10000:
        percent = 12 / 100
    elif sales > 10000:
        percent = 14.5 / 100
    else:
        print('error')
else:
    print('error')

commission = sales * percent

if commission > 0:
    print(f'{commission:.2f}')