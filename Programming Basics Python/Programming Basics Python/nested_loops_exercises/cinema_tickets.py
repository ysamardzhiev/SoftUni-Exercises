input_line = input()

total_tickets_counter = 0
student_tickets_counter = 0
standard_tickets_counter = 0
kids_tickets_counter = 0

while input_line != 'Finish':
    movie_name = input_line
    available_seats = int(input())
    tickets_per_movie = 0
    for i in range(available_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student_tickets_counter += 1
        elif ticket_type == 'standard':
            standard_tickets_counter += 1
        else:
            kids_tickets_counter += 1

        tickets_per_movie += 1
        total_tickets_counter += 1

    room_fill_percent = tickets_per_movie * 100 / available_seats
    print(f"{movie_name} - {room_fill_percent:.2f}% full.")

    input_line = input()

student_tickets_percent = student_tickets_counter * 100 / total_tickets_counter
standard_tickets_percent = standard_tickets_counter * 100 / total_tickets_counter
kids_tickets_percent = kids_tickets_counter * 100 / total_tickets_counter

print(f'Total tickets: {total_tickets_counter}')
print(f'{student_tickets_percent:.2f}% student tickets.')
print(f'{standard_tickets_percent:.2f}% standard tickets.')
print(f'{kids_tickets_percent:.2f}% kids tickets.')