class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class SymbolRepetition(Exception):
    pass


ALLOWED_DOMAINS = ('com', 'bg', 'org', 'net')
MIN_NAME_LENGTH = 4

command = input()
while command != 'End':
    email = command

    if len(email.split('@')[0]) <= MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    elif '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif email.split('.')[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    elif email.count('@') > 1:
        raise SymbolRepetition("Email must contain only one @")

    print("Email is valid")

    command = input()