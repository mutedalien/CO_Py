# Контекстные менеджеры

with open('access_log.log', 'a') as f:
    f.write('New Access')


class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


with open_file('test.log', 'w') as f:
    f.write('Inside `open_file` context manager')
with open_file('test.log', 'r') as f:
    print(f.readlines())
# ['Inside `open_file` context manager']


class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exc_type:
            print('Nothing happend.')
            return True


with suppress_exception(ZeroDivisionError):
    really_big_number = 1 / 0
# Nothing happend.
import contextlib

with contextlib.suppress(ValueError):
    raise ValueError

# Пример на контекстные менеджеры

import time


class timer():
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('Elapsed: {}'.format(self.current_time()))


with timer() as t:
    time.sleep(1)
    print('Current: {}'.format(t.current_time()))
    time.sleep(1)

# Current: 1.0018980503082275
# Elapsed: 2.006608009338379