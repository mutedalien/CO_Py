def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2
for number in even_range(0, 10):
    print(number)
# 0
# 2
# 4
# 6
# 8

def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))
generator = list_generator([1, 2])
next(generator)

def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
        if not value: break
        total += value
generator = accumulator()
print(next(generator))
# 0

print('Accumulated: {}'.format(generator.send(1)))
# Got: 1
# Accumulated: 1

print('Accumulated: {}'.format(generator.send(1)))
# Got: 1
# Accumulated: 2
print('Accumulated: {}'.format(generator.send(1)))
# Got: 1
# Accumulated: 3
next(generator)
# Got: None
