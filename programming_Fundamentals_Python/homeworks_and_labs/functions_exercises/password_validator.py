def is_valid(some_password: str) -> list:
    errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        errors.append('Password must be between 6 and 10 characters')
    if not some_password.isalnum():
        errors.append('Password must consist only of letters and digits')
    digits_counter = 0
    for char in some_password:
        if char.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        errors.append('Password must have at least 2 digits')
    return errors


password = input()
validator = is_valid(password)
if len(validator) == 0:
    print('Password is valid')
else:
    print('\n'.join(validator))