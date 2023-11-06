class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

command = input()
while command != 'Stop':
    commands = command.split()
    some_info = Email(commands[0], commands[1], commands[2])
    emails.append(some_info)
    command = input()

sent_emails = [int(s) for s in input().split(', ')]

for index in sent_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())