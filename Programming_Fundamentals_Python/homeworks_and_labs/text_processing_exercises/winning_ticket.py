def check_ticket(current_ticket):
    if len(current_ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']
    first_half = current_ticket[:10]
    second_half = current_ticket[10:]

    for symbol in winning_symbols:
        if symbol in first_half and symbol in second_half:
            for length in range(10, 5, -1):
                winning_combination = symbol * length
                if winning_combination in first_half and winning_combination in second_half:
                    if length == 10:
                        return f'ticket "{ticket}" - {length}{symbol} Jackpot!'
                    return f'ticket "{ticket}" - {length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [element.strip() for element in input().split(', ')]

for ticket in tickets:
    print(check_ticket(ticket))