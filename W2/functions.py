from datetime import datetime

def get_seconds():
    """Return current seconds"""
    return datetime.now().second
print(get_seconds())
# 42

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())
    return tag_list
print(split_tags('pithon, coursea, mooc'))
# ['pithon', 'coursea', 'mooc']

# по ссылке или по значению?

def extender(source_list, extend_list):
    source_list.extend(extend_list)
values = [1, 2, 3]
extender(values, [4, 5, 6])
print(values)
# [1, 2, 3, 4, 5, 6]

def replacer(source_tuple, replace_with):
    source_tuple = replace_with
user_info = ('Guido', '31/01')
replacer(user_info, ('Larry', '27/09'))
print(user_info)
# ('Guido', '31/01')

# именованные аргументы

def say(greeting, name):
    print('{} {}!'.format(greeting, name))
say('Hello', 'Kitty')
say(name='Kitty', greeting='Hello')
# Hello Kitty!
# Hello Kitty!

# аргументы по умолчанию

def greeting(name='it\'s me...'):
    print('Hello, {}'.format(name))
greeting()
# Hello, it's me...

def append_one(iterable=[]):
    iterable.append(1)
    return iterable
print(append_one([1]))
# [1, 1]
print(append_one())
print(append_one())
# [1]
# [1, 1]
print(append_one.__defaults__)
# ([1, 1],)

# звездочки

def printer(*args):
    print(type(args))
    for argument in args:
        print(argument)
printer(1, 2, 3, 4, 5)
# <class 'tuple'>
# 1
# 2
# 3
# 4
# 5

name_list = ['John', 'Bill', 'Amy']
printer(*name_list)
# <class 'tuple'>
# John
# Bill
# Amy

def printer(**kwards):
    print(type(kwards))
    for key, value in kwards.items():
        print('{}: {}'.format(key, values))
printer(a=10, b=11)
# <class 'dict'>
# a: [1, 2, 3, 4, 5, 6]
# b: [1, 2, 3, 4, 5, 6]

payload = {
    'user_id': 117,
    'feedback': {
        'subject': 'Registration fields',
        'message': 'There is no country for old men'
    }
}
printer(**payload)
# <class 'dict'>
# user_id: [1, 2, 3, 4, 5, 6]
# feedback: [1, 2, 3, 4, 5, 6]
