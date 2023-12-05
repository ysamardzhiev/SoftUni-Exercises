command_line = input()

while command_line != "Welcome!":
    name = command_line
    house = ""

    if name == "Voldemort":
        break

    if len(name) < 5:
        house = "Gryffindor"
    elif len(name) == 5:
        house = "Slytherin"
    elif len(name) == 6:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"

    print(f"{name} goes to {house}.")

    command_line = input()

if command_line != 'Voldemort':
    print("Welcome to Hogwarts.")
else:
    print("You must not speak of that name!")