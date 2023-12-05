deck_of_cards = input().split()
shuffles_count = int(input())

middle_of_the_deck = len(deck_of_cards) // 2

for shuffle in range(shuffles_count):
    deck_after_shuffle = []
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    for card_index in range(middle_of_the_deck):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    deck_of_cards = deck_after_shuffle
print(deck_of_cards)