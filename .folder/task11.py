# Дано натуральное число А>1. Определите каким по счету числом фибониччи оно является, тоесть выведите такое число n, что ф(n) = A
# Если А не является числом фибоначчи, выведите число - 1
A = int (input("Введите число: "))
first_element, second_element, current = 0, 1, 1
count = 2
while current < A:
    current = first_element + second_element
    first_element = second_element
    second_element = current
    count+=1

if current == A:
    print(f"Элемент фибоначчи {count}")
else:
    print(-1)