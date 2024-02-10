def age_assignment(*names, **kwargs):
    people = {name: kwargs[name[0]] for name in names}
    return '\n'.join(f'{name} is {age} years old.' for name, age in sorted(people.items()))


print(age_assignment("Peter", "George", G=26, P=19))