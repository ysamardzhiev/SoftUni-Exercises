users = {}
languages = {}

command = input()
while command != 'exam finished':
    commands = command.split('-')
    username = commands[0]
    if len(commands) == 2:
        users.pop(username)
        command = input()
        continue
    language = commands[1]
    points = int(commands[2])
    if username not in users:
        users[username] = 0
    if points > users[username]:
        users[username] = points
    if language not in languages:
        languages[language] = 0
    languages[language] += 1
    command = input()
print('Results:')
for user, points in users.items():
    print(f'{user} | {points}')
print('Submissions:')
for language, submissions in languages.items():
    print(f'{language} - {submissions}')