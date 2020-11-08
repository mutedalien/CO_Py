# Создание экземпляра (объекта) класса

class Planet:
    pass

planet = Planet()
print(planet)
# <__main__.Planet object at 0x00000275D6849460>

solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print(solar_system)
# [<__main__.Planet object at 0x000002477172F9D0>,
# <__main__.Planet object at 0x00000247716F9460>,
# <__main__.Planet object at 0x000002477172FA60>,
# <__main__.Planet object at 0x000002477172FE20>,
# <__main__.Planet object at 0x000002477172FF40>,
# <__main__.Planet object at 0x000002477172FE50>,
# <__main__.Planet object at 0x000002477172FB80>,
# <__main__.Planet object at 0x000002477172FB50>]

solar_system = {}
for i in range(8):
    planet = Planet()
    solar_system[planet] = True

print(solar_system)
# {<__main__.Planet object at 0x0000022D627EEFA0>: True,
# <__main__.Planet object at 0x0000022D627EEE20>: True,
# <__main__.Planet object at 0x0000022D627EEFD0>: True,
# <__main__.Planet object at 0x0000022D627EEF70>: True,
# <__main__.Planet object at 0x0000022D627EEF10>: True,
# <__main__.Planet object at 0x0000022D627EEEB0>: True,
# <__main__.Planet object at 0x0000022D627EEE80>: True,
# <__main__.Planet object at 0x0000022D627EEE50>: True}

# Инициализация экземпляра

class Planet:

    def __init__(self, name):
        self.name = name
earth = Planet("Earth")
print(earth.name)
print(earth)
# Earth
# <__main__.Planet object at 0x000001FE942B3970>

class Planet:

    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
earth = Planet("Earth")
print(earth)
# Earth

solar_system = []
planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]
for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
# [<__main__.Planet object at 0x00000273ABB03EB0>,
# <__main__.Planet object at 0x00000273ABB03E50>,
# <__main__.Planet object at 0x00000273ABB03FD0>,
# <__main__.Planet object at 0x00000273ABB03FA0>,
# <__main__.Planet object at 0x00000273ABB038E0>,
# <__main__.Planet object at 0x00000273ABB03670>,
# <__main__.Planet object at 0x00000273ABB03610>,
# <__main__.Planet object at 0x00000273ABB035B0>]

class Planet:

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Planet {self.name}"
solar_system = []
planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]
for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
# [Planet Mercury, Planet Venus, Planet Earth, Planet Mars, Planet Jupiter, Planet Saturn, Planet Uranus, Planet Neptune]

# Работа с атрибутами экземпляра

mars = Planet("Mars")
print(mars)
# Planet Mars

mars.name = "Second Earth?"
print(mars.name)
# Second Earth?

# Атрибуты класса

class Planet:
    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1
earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)
# 2
print(mars.count)
# 2

# Деструктор экземпляра класса

class Human:

    def __del__(self):
        print("Goodbye!")
human = Human()
# в данном случае деструктор отработает - но все же
# лучше создать метод и вызывать его явно
del human
# Goodbye!

# Словарь экземпляра и класса

class Planet:
    """This class describes planets"""

    count = 1
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
planet = Planet("Earth")
print(planet.__dict__)
# {'name': 'Earth', 'population': []}
planet.mass = 5.97e24
print(planet.__dict__)
# {'name': 'Earth', 'population': [], 'mass': 5.97e+24}
print(Planet.__dict__)
# {'__module__': '__main__', '__doc__': 'This class describes planets', 'count': 1,
# '__init__': <function Planet.__init__ at 0x000001C86C8ED280>, '__dict__': <attribute
# '__dict__' of 'Planet' objects>, '__weakref__': <attribute '__weakref__' of 'Planet' objects>}
print(dir(planet))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'count', 'mass', 'name', 'population']