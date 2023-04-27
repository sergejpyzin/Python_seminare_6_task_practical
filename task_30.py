# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

count_number = int(input("Введите кол-во членов прогрессии: "))
first_number = int(input("Введите первый член (начало) прогрессии: "))
diff_number = int(input("Введите разность членов прогрессии: "))
# some_list = []
# some_list[0] = first_number
# for i in range(first_number + diff_number, count_number + 1):
#
#     some_list.append()

print(list(range(first_number, count_number * diff_number + 1, diff_number)))