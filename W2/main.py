# Списки

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
