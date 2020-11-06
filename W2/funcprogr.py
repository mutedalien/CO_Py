def caller(func, params):
    return func(*params)
def printer(name, origin):
    print('I\'m {} of {}!'.format(name, origin))
caller(printer, ['Moana', 'Motunui'])
# I'm Moana of Motunui!

def get_multiplier():
    def inner(a, b):
        return a * b
    return inner
multiplier = get_multiplier()
print(multiplier(10, 11))
# 110

print(multiplier.__name__)
# inner

def get_multiplier(number):
    def inner(a):
        return a * number
    return inner
multiplier_by_2 = get_multiplier(2)
print(multiplier_by_2(10))
# 20

# map, filter, lambda

def squarify(a):
    return a ** 2
print(list(map(squarify, range(5))))
# [0, 1, 4, 9, 16]

squared_list = []
for number in range(5):
    squared_list.append(squarify(number))
print(squared_list)
# [0, 1, 4, 9, 16]

def is_positive(a):
    return a > 0
print(list(filter(is_positive, range(-2, 3))))
# [1, 2]

positive_list = []
for number in range(-2, 3):
    if is_positive(number):
        positive_list.append(number)
print(positive_list)
# [1, 2]

print(list(map(lambda x: x ** 2, range(5))))
# [0, 1, 4, 9, 16]

print(type(lambda x: x ** 2))
# <class 'function'>

# Упражнение: написать функцию, которая превращает список чисел в список строк.

def stringify_list(num_list):
    return list(map(str, num_list))
print(stringify_list(range(10)))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

from functools import reduce
def multiply(a, b):
    return a * b
print(reduce(multiply, [1, 2, 3, 4, 5]))
# 120

from functools import partial
def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)
hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')
print(hier('brother'))
print(helloer('sir'))
# Hi, brother!
# Hello, sir!

square_list = []
for number in range(10):
    square_list.append(number ** 2)
print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

square_list = [number ** 2 for number in range(10)]
print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)
# [0, 2, 4, 6, 8]

square_map = {number: number ** 2 for number in range(5)}
print(square_map)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

reminders_set = {num % 10 for num in range(100)}
print(reminders_set)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(type(number ** 2 for number in range(5)))
# <class 'generator'>

num_list = range(7)
squared_list = [x ** 2 for x in num_list]
print(list(zip(num_list, squared_list)))
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
))
print(list)
# <class 'list'>
# [(1, 1), (2, 2)]