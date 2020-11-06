def decorator(func):
    return func

@decorator # синтаксис декоратора
def decorated():
    print('Hello!')


def decorator(func):
    def new_func():
        pass
    return new_func
@decorator
def decorated():
    print('Hello!')
decorated()
print(decorated.__name__)
# new_func

def stringify(func):
  return str(func)
@stringify
def multiply(a, b):
  return a * b
# вернет ошибку

def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped
@logger
def summator(num_list):
    return sum(num_list)
print('Summator: {}'.format(summator([1, 2, 3, 4])))
# Summator: 10

print('Summator: {}'.format(summator([1, 2, 3, 4])))
# Summator: 10

def logger(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped
print(summator.__name__)
# wrapped

import functools
def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped
@logger
def summator(num_list):
    return sum(num_list)
print(summator.__name__)
# summator

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result

        return wrapped

    return decorator


@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)


# без синтаксического сахара:
# summator = logger('log.txt')(summator)

summator([1, 2, 3, 4, 5, 6])
with open('new_log.txt', 'r') as f:
    print(f.read())
# 21

# Посмотрим, что будет, если применить сразу несколько декораторов:
def first_decorator(func):
    def wrapped():
        print('Inside first_decorator product')
        return func()
    return wrapped
def second_decorator(func):
    def wrapped():
        print('Inside second_decorator product')
        return func()
    return wrapped

@first_decorator
@second_decorator
def decorated():
    print('Finally called...')
# то же самое, но без синтаксического сахара:
# decorated = first_decorator(second_decorator(decorated))
decorated()
# Inside first_decorator product
# Inside second_decorator product
# Finally called...

def bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped
def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped
@bold
@italic
def hello():
    return "hello world"
# hello = bold(italic(hello))
print(hello())
# <b><i>hello world</i></b>