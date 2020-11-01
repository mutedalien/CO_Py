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

# Логические типы
result = True
print(type(result))

# Операции сравнения
print(3 > 4)
print(3 <= 3)
print(3 >= 6)
print(3 < 5)

x = 2
print(1 < x < 3)

# Логические выражения
x, y = True, False
print(x and y)

x, y = True, False
print(x or y)

y = False
print(not y)

# Составные логические выражения
x, y, z = True, False, True
result = x and y or z
print(result)

x = 12
y = False
print(x or y)

x = 12
z = "BOOM"
print(x and z)

# Задача: определить високосный год или нет?
# Год является високосным, если он кратен 4, но при этом не кратен 100, либо кратен 400
year = 2020
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)
# или еще короче
import calendar
print(calendar.isleap(2020))

# БАЗОВЫЕ ТИПЫ
# Строки (str)

example_string = "Курс по Python на Coursea"
print(example_string)
print(type(example_string))
example_string = 'Курс по "Python" на "Coursea"'
print(example_string)
example_string = "Курс по \"Python\" на \"Coursea\""
print(example_string)
example_string = "Файл на диске c:\\\\"
print(example_string)
example_string = r"Файл на диске c:\\"
print(example_string)
example_string = "Perl - это язык, который одинаково " \
                "выглядет как до, так и после RSA шифрования." \
                "(Keith Bostic)"
print(example_string)

example_string = """
Есть всего два типа языков программирования: те, на которые
люди все время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""
print(example_string)

"Можно просто " + "складывать строки"
"Даже умножать!" * 3

# Строки неизменяемые (при изменении создается новый объект
example_string = "Привет"
print(id(example_string))
example_string = ", Мир!"
print(id(example_string))

# Срезы строк
example_string = "Курс про Python на Coursea"
print(example_string[9:])

example_string = "Курс про Python на Coursea"
print(example_string[9:15])

example_string = "Курс про Python на Coursea"
print(example_string[-8:])

example_string = "0123456789"
print(example_string[::2])

example_string = "Москва"
print(example_string[::-1])

quote = """Болтовня ничего не стоит. Покажите мне код. 
Linus Torvalds
"""
print(quote.count("о"))

"москва".capitalize()
"2020".isdigit()

# Оператор in позволяет проверить наличие подстроки в строке:
"3.14" in "Число Пи = 3,1415926"
# True
"Алексей" in "Александр Пушкин"
# False

# Итерация по строке
example_string = "Привет"
for letter in example_string:
    print("Буква", letter)

# Форматирование строк
template = "%s - главное достоинство программистаю (%s)"
template % ("Лень", "Larry Wall")
# 'Лень - главное достоинство программистаю (Larry Wall)'
"{} не лгут, но {} пользуются формулами. ({})".format(
    "Цифры", "лжецы", "Robert A. Heinlein"
)
# 'Цифры не лгут, но лжецы пользуются формулами. (Robert A. Heinlein)'

# И еще f-строки
subject = "оптимизация"
autor = "Donald Knuth"
f"Преждевременная {subject} - корень всех зол. ({autor})"
# 'Преждевременная оптимизация - корень всех зол. (Donald Knuth)'

# Модификаторы форматирования:
num = 8
print(f"Binary: {num:#b}")
# 'Binary: 0b1000'
num = 2/3
print(num)
print(f"{num:.3f}")
# 0.6666666666666666
# 0.667

# Встроенная функция input()
name = input("Введите свое имя: ")
print(f"Привет, {name}!")

# Байтовые строки (bytes)
example_bytes = b"hello"
print(type(example_bytes))

for element in example_bytes:
    print(element)

example_string = "привет"
print(type(example_string))
print(example_string)
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))