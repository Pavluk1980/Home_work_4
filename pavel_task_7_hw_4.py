'''Задача 7. 10 баллов

Написать программу которая данный список кортежей переведет в список списков

Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]'''


spis_kort = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)] # заданный "список кортежей"
print('Заданный "список кортежей":     ', spis_kort)
a = len(spis_kort) # находим кол-во элементов списка
spis_spis = [0] * a # создаем нулевой "список списков"
for i in range(0,a): # создаем цикл по количеству элементов списка
    spis_spis[i] = list(spis_kort[i]) # преобразуем элементы списка "кортеж" в элемента списка "список"
print('Полученный "список списков":  ', spis_spis)
