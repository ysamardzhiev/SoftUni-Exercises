exam_statistics = {}

command = input()
while command != 'exam finished':
    commands = command.split('-')
    username = commands[0]

    if commands[1] == 'banned':
        for language in exam_statistics.keys():
            if username in exam_statistics[language].keys():
                exam_statistics[language][username]['banned_status'] = True
        command = input()
        continue

    language, points = commands[1], int(commands[2])
    if language not in exam_statistics.keys():
        exam_statistics[language] = {}
    if username not in exam_statistics[language].keys():
        exam_statistics[language][username] = {'points': 0, 'submissions': 0, 'banned_status': False}
    if points > exam_statistics[language][username]['points']:
        exam_statistics[language][username]['points'] = points
    exam_statistics[language][username]['submissions'] += 1
    command = input()

print('Results:')
for language, users in exam_statistics.items():
    for user in users.keys():
        if not exam_statistics[language][user]["banned_status"]:
            print(f'{user} | {exam_statistics[language][user]["points"]}')
print('Submissions:')
for language, users in exam_statistics.items():
    total_submissions = 0
    for user in users.keys():
        total_submissions += exam_statistics[language][user]['submissions']
    print(f'{language} - {total_submissions}')