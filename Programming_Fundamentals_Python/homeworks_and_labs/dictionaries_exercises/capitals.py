countries = input().split(', ')
capitals = input().split(', ')

countries_and_capitals = dict(zip(countries, capitals))

for country, capital in countries_and_capitals.items():
    print(f'{country} -> {capital}')