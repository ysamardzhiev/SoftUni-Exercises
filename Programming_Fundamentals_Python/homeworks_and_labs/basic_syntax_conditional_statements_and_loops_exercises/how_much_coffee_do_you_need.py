current_string = input()

number_of_coffees = 0

while current_string != 'END':

    if current_string.lower() == 'coding' \
            or current_string.lower() == 'dog' \
            or current_string.lower() == 'cat' \
            or current_string.lower() == 'movie':
        if current_string.islower():
            number_of_coffees += 1
        else:
            number_of_coffees += 2

    current_string = input()

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)