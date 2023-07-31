# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random
list1 = []
for _ in range(10):
    list1.append(random.randint(0,5))

list2 = []

for i in list1:
    if not (i in list2):
        list2.append(i)
print(list1)
print(len(list2))
# print(len(set(list1))) преобразовали в множество и взяли его размер
