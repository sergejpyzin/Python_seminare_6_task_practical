# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

minimum_range = int(input("Введите минимум диапазона: "))
maximum_range = int(input("Введите максимум диапазона: "))
length_list = int(input("Введите длинну массива: "))
some_list = [random.randint(minimum_range - 20, maximum_range + 20) for i in range(length_list)]
result_list = []

for i in range(len(some_list)):
    if minimum_range < some_list[i] < maximum_range:
        result_list.append(i)

print(some_list)
print(result_list)