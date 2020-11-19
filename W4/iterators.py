Итераторы
for number in range(5):
    print(number & 1)
# 0
# 1
# 0
# 1
# 0
for letter in 'python':
    print(ord(letter))
# 112
# 121
# 116
# 104
# 111
# 110
iterator = iter([1, 2, 3])
print(next(iterator))
# 1
print(next(iterator))
# 2
print(next(iterator))
# 3

class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


for num in SquareIterator(1, 4):
    print(num)
# 1
# 4
# 9


class IndexIterable:
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]


for letter in IndexIterable('str'):
    print(letter)
# s
# t
# r