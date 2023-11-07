class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\n" \
                   f"Total animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\n" \
                   f"Total animals: {Zoo.__animals}"
        else:
            return f"Birds in {self.name}: {', '.join(self.birds)}\n" \
                   f"Total animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

type_of_species = input()
print(zoo.get_info(type_of_species))