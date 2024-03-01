import os

command = input()
while command != 'End':
    action, file_name, *additional = command.split('-')
    path = os.path.join('files', file_name)

    if action == 'Create':
        with open(path, 'w'):
            pass
    elif action == 'Add':
        with open(path, 'a') as file:
            file.write(f"{additional[0]}\n")
    elif action == 'Replace':
        if os.path.exists(path):
            old_str, new_str = additional[0], additional[1]
            with open(path, 'r') as file:
                content = file.read()

            with open(path, 'w') as file:
                content = content.replace(old_str, new_str)
                file.write(content)
        else:
            print("An error occurred")
    elif action == 'Delete':
        try:
            os.remove(path)
        except FileNotFoundError:
            print("An error occurred")

    command = input()
