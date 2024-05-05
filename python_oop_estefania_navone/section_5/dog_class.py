class Dog:

    species = 'Canis lupus'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


ray = Dog('Ray', 1, 'Spitz')
print(Dog.species)
