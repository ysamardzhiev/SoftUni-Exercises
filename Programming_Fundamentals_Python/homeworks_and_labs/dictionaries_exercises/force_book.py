force_book = {}

command = input()
while command != 'Lumpawaroo':
    user_is_added = False
    if '|' in command:
        force_side, force_user = command.split(' | ')
        for users in force_book.values():
            if force_user in users:
                user_is_added = True
                break
        if not user_is_added:
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)
    else:
        force_user, force_side = command.split(' -> ')
        for users in force_book.values():
            if force_user in users:
                users.remove(force_user)
                break
        if force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')
    command = input()

for force_side, force_users in force_book.items():
    if not force_users:
        continue
    print(f'Side: {force_side}, Members: {len(force_users)}')
    for user in force_users:
        print(f"! {user}")