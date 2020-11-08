# Работа с методами экземпляра
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)
mars = Planet("Mars")
bob = Human("Bob")
mars.add_human(bob)
# Welcome to Mars, Bob!
print(mars.population)
# [<__main__.Human object at 0x0000020ECDAFEF10>]