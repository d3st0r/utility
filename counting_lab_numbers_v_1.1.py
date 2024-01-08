# Записывает количество чисел
n = int(input('Количество чисел: '))
# Список для чисел измерений
l1 = []
l1_str = ''
# Список для чисел отклонений
l2 = []
l2_str = ''
# Список для чисел квадратных отклонений
l3 = []
l3_str = ''
for _ in range(n):
    num = float(input('Введите число: '))
    l1.append(num)
# Переменная среднего числа
average = round(sum(l1)/len(l1), 5)
# Добавляет значения разности числа измерения и среднего числа
for j in range(len(l1)):
    l2.append(round((l1[j] - average), 5))
# Переменная суммы всех чисел отклонений
sum_deviation = round(sum(l2), 5)
# Добавляет значения квадрата разности числа измерения и среднего числа
for j in range(len(l1)):
    l3.append(round(((l1[j] - average) ** 2), 5))
# Переменная квадрата суммы всех чисел отклонений
sum_square_deviation = round((sum(l3)), 5)
# Вывод таблицы чисел измерений
print()
print()
print('Таблица чисел')
for i_table1 in l1:
    l1_str = str(i_table1)
    print(l1_str, end='\t')
print()
print()
# Вывод таблицы разности чисел отклонений
print('Таблица отклонений\t')
for i_table2 in l2:
    l2_str = str(i_table2)
    print(l2_str, end='\t')
print()
print()
# Вывод таблицы квадратной разности чисел отклонений
print('Таблица квадратичных отклонений\t')
for i_table3 in l3:
    l3_str = str(i_table3)
    print(l3_str, end='\t')
print()
print()
# Вывод среднего числа
print('Среднее число: ', average)
# Вывод суммы чисел отклонений
print('Сумма отклонений', sum_deviation)
# Вывод квадратной суммы чисел отклонений
print('Сумма квадратичных отклонений', sum_square_deviation)
