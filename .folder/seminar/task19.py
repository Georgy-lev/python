# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

list = []
for i in range(10):
    list.append(i)

k = int(input("enter k: "))
print(list)

# list = list[-k:]+list[:-k]
# print(list)

for _ in range(k):
    list.insert(0, list.pop())
print(list)