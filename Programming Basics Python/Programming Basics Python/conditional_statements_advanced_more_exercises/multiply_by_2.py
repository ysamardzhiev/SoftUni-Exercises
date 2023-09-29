number = 0

while number > 0:
    counter = number * 2
    print(f'{counter:.2f}')
    if counter < 0:
        break
        print('Negative number!')