import random

numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))
print(numbers)
# [14, 16, 19, 17, 18, 15, 20, 11, 16, 12, 12]

numbers.sort()

half_size = len(numbers) // 2 # берем половину
median = None

if numbers_size % 2 == 1: # если четный
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2 # срез от -1 до +1 и берем среднеарифм /2
print(median)
# 16
import statistics
print(statistics.median(numbers))
# 16