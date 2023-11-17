force_book = {}

user_is_not_added = False

command = input()
while command != 'Lumpawaroo':
    if '|' in command:
        data = command.split(' | ')
        force_side = data[0]
        force_user = data[1]
        if force_side not in force_book.keys():
            force_book[force_side] = []
        for users in force_book.values():
            if force_user not in users:
                user_is_not_added = True
            else:
                user_is_not_added = False
                break
        if user_is_not_added:
            force_book[force_side].append(force_user)
    else:
        data = command.split(' -> ')
        force_user = data[0]
        force_side = data[1]
        if force_side not in force_book.keys():
            force_book[force_side] = []

        for users in force_book.values():
            if force_user not in users:
                user_is_not_added = True
            else:
                user_is_not_added = False
                users.remove(force_user)
                break
        if user_is_not_added:
            force_book[force_side].append(force_user)
        else:
            force_book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')
    command = input()

for force_side, force_users in force_book.items():
    if not force_users:
        continue
    print(f'Side: {force_side}, Members: {len(force_users)}')
    for user in force_users:
        print(f"! {user}")