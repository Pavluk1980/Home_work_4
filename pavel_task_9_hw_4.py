"""
Задача 9. 10 баллов

Тема Листы

Даны два списка элементов если хоть один елемент совпадает отпринтить True.

print(Тrue) не слово! а объект подставить.
"""
stroka_1 = (input('введитите список 1 через пробел: ').split(' ')) # получаем строку ввода 1 и первеодим в список 1
stroka_2 = (input('введитите список 2 через пробел: ').split(' ')) # получаем строку ввода 2 и первеодим в список 2
spis_1 = list(set(stroka_1)) # оставляем только уникальные элементы в списке 1
spis_2 = list(set(stroka_2)) # оставляем только уникальные элементы в списке 2
a = len(spis_1) # определяем длину списка 1
b = len(spis_2) # определяем длину списка 2
counter = 0 # вводим переменную для счетчика совпадений
for i in range(0,a): # цикл для перебора элементов списка 1
    for c in range(0,b): # цикл для перебора элементов списка 2
        if spis_1[i] == spis_2[c]: # поиск взаимных совпадений
            print(f'элемент "{spis_1[i]}" имеет взаимное совпадение в обоих списках') # уведомление в случае наличия взаимных совпадений
            counter +=1 # счетчик совпадений

if counter == 0:
    print('В заданных списках взаимных совпадений не найдено.') # уведомление в случае отсутствия совпадений