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
print(reversed(numbers))
print(list(reversed(numbers)))
"""
[2, 12, 16, 2, 11, 7, 12, 12, 14, 19]
[2, 2, 7, 11, 12, 12, 12, 14, 16, 19]
[2, 12, 16, 2, 11, 7, 12, 12, 14, 19]
[19, 16, 14, 12, 12, 12, 11, 7, 2, 2]
[19, 16, 14, 12, 12, 12, 11, 7, 2, 2]
<list_reverseiterator object at 0x000001AE31458F40>
[2, 2, 7, 11, 12, 12, 12, 14, 16, 19]
"""

# КОРТЕЖИ

# empty_tuple = ()
# empty_tuple = tuple()
# immutables = (int, str, tuple)
# immutables[0] = float
# вернет ошибку, т.к. они не изменяемые!

blink = ([], [])
blink[0].append(0)
print(blink)
# ([0], [])
print(hash(tuple()))
# 5740354900026072187

one_element_tuple = (1,)
guess_what = (1)
print(type(guess_what))
# <class 'int'>