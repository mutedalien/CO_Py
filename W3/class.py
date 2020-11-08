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