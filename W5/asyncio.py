# Неблокирующий ввод/вывод, обучающий пример

import socket
import select

sock = socket.socket()
sock.bind(("", 10001))
sock.listen()

# как обработать запросы для conn1 и conn2
# одновременно без потоков?
conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)
conn2.setblocking(0)

epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,
}
# Неблокирующий ввод/вывод, обучающий пример
# Цикл обработки событий в epoll

while True:
    events = epoll.poll(1)

    for fileno, event in events:
        if event & select.EPOLLIN:
            # обработка чтения из сокета
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            # обработка записи в сокет
            conn_map[fileno].send("pong".encode("utf8"))


# Итераторы

class MyRangeIterator:
    def __init__(self, top):
        self.top = top
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.top:
            raise StopIteration

        current = self.current
        self.current += 1
        return current

# >>> counter = MyRangeIterator(3)
# >>> counter
# < __main__.MyRangeIterator object at 0xb671b5cc >
# >>> for it in counter:
# >>> print(it)
# 0
# 1
# 2

# Генераторы

def my_range_generator(top):
    current = 0
    while current < top:
        yield current
        current += 1

# >>> counter = my_range_generator(3)
# >>> counter
# <generator object my_range_generator at 0xb67170ec>
# >>> for it in counter:
# >>>     print(it)
# 0
# 1
# 2

# Сопрограммы, генерация исключений

def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")

# >>> g = grep("python")
# >>> next(g) # g.send(None)
# >>> g.send("python is the best!")
# >>> g.throw(RuntimeError, "something wrong")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# RuntimeError: something wrong

# Вызовы сопрограмм, PEP 380

def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)

def grep_python_coroutine():
    g = grep("python")
    next(g)
    g.send("python is the best!")
    g.close()

# >>> g = grep_python_coroutine()  # is g coroutine?
# start grep
# python is the best!
# >>> g
# >>>

# Сопрограммы, yield from PEP 0380

def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)

def grep_python_coroutine():
    g = grep("python")
    yield from g

# >>> g = grep_python_coroutine()  # is g coroutine?
# >>> g
# <generator object grep_python_coroutine at 0x7f027eec03b8>
# >>> g.send(None)
# start grep
# >>> g.send("python wow!")
# python wow!

# PEP 380, генераторы

def chain(x_iterable, y_iterable):
    yield from x_iterable
    yield from y_iterable


def the_same_chain(x_iterable, y_iterable):
    for x in x_iterable:
        yield x

    for y in y_iterable:
        yield y

# >>> a = [1, 2, 3]
# >>> b = (4, 5)
# >>> for x in chain(a, b):
# ...    print(x)
# 1
# 2
# 3
# 4
# 5