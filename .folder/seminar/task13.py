# Пользователь вводит число N - общее количество
# рассатриваемых дней (1< N < 100). в следующих строках
# распологается N целых чисел.
# каждое число - среднесуточная температура в 
# соответствубщий день. Температуры - целые числа и лежат в 
# диапазоне от - 50 до 50

import random

amount_days = int(input())
temps = []

for i in range(amount_days):
    temps.append(random.randint(-50, 50))
count_max_warm = 0
count = 0
for i in temps:
    if i>0:
        count += 1
    else:
        if count_max_warm < count:
            count_max_warm = count
            count = 0
print(temps)
print(count)
