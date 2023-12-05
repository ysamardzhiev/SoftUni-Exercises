elements = input().split()

moves_counter = 0
command = input()
while elements and command != 'end':
    elements_indexes = command.split()
    index1 = int(elements_indexes[0])
    index2 = int(elements_indexes[1])
    moves_counter += 1
    if index1 == index2 or 0 > index1 or index1 >= len(elements) or 0 > index2 or index2 >= len(elements):
        middle_index = len(elements) // 2
        elements.insert(middle_index, f"-{moves_counter}a"), elements.insert(middle_index, f"-{moves_counter}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            if index1 > index2:
                elements.pop(index1), elements.pop(index2)
            else:
                elements.pop(index2), elements.pop(index1)
        else:
            print("Try again!")
    command = input()
if elements:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
else:
    print(f"You have won in {moves_counter} turns!")