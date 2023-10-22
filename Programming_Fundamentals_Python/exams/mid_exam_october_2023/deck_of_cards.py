cards_deck = input().split(', ')
n = int(input())

for current_turn in range(n):
    commands = input().split(', ')
    type_of_command = commands[0]
    if type_of_command == 'Add':
        card = commands[1]
        if card not in cards_deck:
            cards_deck.append(card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif type_of_command == 'Remove':
        card = commands[1]
        if card in cards_deck:
            cards_deck.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif type_of_command == 'Remove At':
        index = int(commands[1])
        if 0 <= index < len(cards_deck):
            cards_deck.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif type_of_command == 'Insert':
        index = int(commands[1])
        card = commands[2]
        if 0 <= index < len(cards_deck) and card in cards_deck:
            print("Card is already added")
        elif 0 <= index < len(cards_deck):
            cards_deck.insert(index, card)
            print("Card successfully added")
        else:
            print("Index out of range")
print(', '.join(cards_deck))