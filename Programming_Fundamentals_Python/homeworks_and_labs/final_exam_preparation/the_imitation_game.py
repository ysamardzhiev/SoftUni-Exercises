encrypted_message = input()

command = input()
while command != 'Decode':
    instructions = command.split('|')
    if instructions[0] == 'Move':
        number_of_letters = int(instructions[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif instructions[0] == 'Insert':
        index, value = int(instructions[1]), instructions[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    else:
        substring, replacement = instructions[1], instructions[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")