empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}
print(collections_map)
# {'mutable': ['list', 'set', 'dict'], 'immutable': ['tuple', 'frozenset']}
print(collections_map['immutable'])
# ['tuple', 'frozenset']
print(collections_map.get('irresistible', 'not found'))
# not found

beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar',
}
print(beatles_map)
# {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}

beatles_map['Ringo'] = 'Drums'
print(beatles_map)
# {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar', 'Ringo': 'Drums'}

del beatles_map['John']
print(beatles_map)
# {'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums'}

beatles_map.update({
    'John': 'Guitar'
})
print(beatles_map)
# {'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums', 'John': 'Guitar'}

print(beatles_map.pop('Ringo'))
# Drums
print(beatles_map)
# {'Paul': 'Bass', 'George': 'Guitar', 'John': 'Guitar'}

unknow_dict = {}
print(unknow_dict.setdefault('key', 'default'))
# default

print(unknow_dict)
# {'key': 'default'}

print(unknow_dict.setdefault('key', 'new_default'))
# default

# ИТЕРАЦИЯ

print(collections_map)
# {'mutable': ['list', 'set', 'dict'], 'immutable': ['tuple', 'frozenset']}
for key in collections_map:
    print(key)
# mutable
# immutable

for key, value in collections_map.items():
    print('{} - {}'.format(key, value))
# mutable - ['list', 'set', 'dict']
# immutable - ['tuple', 'frozenset']

# OrderDict

from collections import OrderedDict

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)
for key in ordered:
    print(key)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
