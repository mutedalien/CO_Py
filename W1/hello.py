# Comment

"""
Многострочный
комментарий
"""

print("Hello, world!") # Comment

for i in range(4):
    print(i)

num = 13
print(num)

num = 0
print(num)

num = 10
print(num)

num = 13
print(type(num))

num = 13.4
print(num)

num = 0.0
print(num)

num = -10.2
print(num)
print(type(num))

num = 100_000.000_001
print(num)

# 1,5 умножить на 10 в степени 2
num = 1.5e2
print(num)

# Конвертация типов
num = 150.2
print(type(num))

num = int(num)
print(num, type(num))

num = float(num)
print(num, type(num))

# Комплексные числа (complex)
num = 14 + 1j

print(type(num))
print(num.real)
print(num.imag)

# Математика
print(10 * 3 + 3)
print(10 * (3 + 3))

# print(100 / (100 % 1)) # Исключение

# Побитовые операции
x = 4
y = 3

print("Побитовое или: ", x | y)
print("Побитовое исключающее или: ", x ^ y)
print("Побитовое и: ", x & y)
print("Битовый сдвиг влево: ", x << 3)
print("Битовый сдвиг вправо: ", x >> 1)
print("Инверсия битов: ", ~x)

# Декартовые координаты (найти гипотенузу прямоугольного треугольника)
x1, y1 = 0, 0
x2 = 3
y2 = 4

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)

# Меняем местами значение двух переменных
a = 100
b = 200
print(a, b)

a, b = b, a
print(a, b)
