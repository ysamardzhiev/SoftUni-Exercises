class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()
while command != 'End':
    try:
        name, email = command.split('@')
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif not any(domain in email for domain in ['com', 'bg', 'org', 'net']):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    command = input()