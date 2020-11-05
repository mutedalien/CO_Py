# СПИСКИ

empty_list = []
empty_list = list()

non_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]
print(len(collections))
# 4
print(collections)
# ['list', 'tuple', 'dict', 'set']
print(collections[0])
# list
print(collections[-1])
# set

collections[3] = 'frozenset'
print(collections)
# ['list', 'tuple', 'dict', 'frozenset']

range_list = list(range(10))
print(range_list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_list[1:3])
# [1, 2]
print(range_list[3:])
# [3, 4, 5, 6, 7, 8, 9]
print(range_list[:5])
# [0, 1, 2, 3, 4]
print(range_list[::-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(range_list[5:1:-1])
# [5, 4, 3, 2]
range_list[:] is range_list
# False

# ИТЕРАЦИИ

collections = ['list', 'tuple', 'dict', 'set']
for collection in collections:
    print('Learning {}...'.format(collection))
"""
Learning list...
Learning tuple...
Learning dict...
Learning set...
"""
for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))
"""
#0 list
#1 tuple
#2 dict
#3 set
"""

# ДОБАВЛЕНИЕ И УДАЛЕНИЕ ЭЛЕМЕНТОВ

collections.append('OrderedDict')
print(collections)
# ['list', 'tuple', 'dict', 'set', 'OrderedDict']
collections.extend(['ponyset', 'unicorndict'])
print(collections)
# ['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict']
collections += [None]
print(collections)
# ['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict', None]
del collections[4]
print(collections)
# ['list', 'tuple', 'dict', 'set', 'ponyset', 'unicorndict', None]

# min, max, sum

numbers = [4, 17, 19, 9, 2, 6, 10, 13]
print(min(numbers))
# 2
print(max(numbers))
# 19
print(sum(numbers))
# 80

# str.join

tag_list = ['python', 'course', 'coursea']
print(', '.join(tag_list))
# python, course, coursea

# СОРТИРОВКА

import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 20))
print(numbers)
print(sorted(numbers))
print(numbers)
print(sorted(numbers, reverse=True))
numbers.sort(reverse=True)
print(numbers)
"""
[6, 20, 18, 17, 12, 4, 10, 4, 18, 20]
[4, 4, 6, 10, 12, 17, 18, 18, 20, 20]
[6, 20, 18, 17, 12, 4, 10, 4, 18, 20]
[20, 20, 18, 18, 17, 12, 10, 6, 4, 4]
[20, 20, 18, 18, 17, 12, 10, 6, 4, 4]
"""
