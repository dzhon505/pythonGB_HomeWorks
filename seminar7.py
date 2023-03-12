# list comprehension
# a = [i if i % 2 == 0 else 0 for i in range(1, 9)]
# print(a)

# enumerate
# a = [0,2,0,4,0,6,0,8]
# for indx, value in enumerate(a):
#     print(indx,value)

# lambda
# def summa(a,b):
#     return a+b
# print(summa(3,4))

# summa = lambda a,b:a+b
# print(summa(3,4))

# map

# a = [12,24,2,67,55]
# print(list(map(lambda x: x*2 if x%2 == 0 else 1, a)))

# filter

# a = [12,3,45,6]
# a1 = [12,3,45,6]
# a = list(filter(lambda x: x%2==0,a))
# a1 = list(filter(lambda x: True if x*2>20 else False, a1))
# print(a)
# print(a1)

# zip

# a = [1,2,3,4]
# b = 'abcdef'
# d = {1:'34', 2:'34324', 5:'123'}
# res = list(zip(a,b,d))
# print(res)
#
# z = [1,2,3,4]
# x = 'abcdef'
# c = dict(zip(a, b))
# print(c)



# Задача №47.
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_values = list(map(lambda x: x, values))
# if values == new_values:
#     print('ok')
# else:
#     print('error')

# Задача №49.
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# import math
# def find_farthest_orbits(orbits):
#     return max(orbits, key=lambda x: math.pi*x[0]*x[1] if x[0] != x[1] else 0)
# orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
#
# print(*find_farthest_orbits(orbits))

###################

# def find_farthest_orbits(orbits):
#     return max(orbits, key=lambda x: x[0]*x[1] if x[0] != x[1] else 0)
# orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
#
# print(*find_farthest_orbits(orbits))


# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     return all(map(characteristic, objects))
#
# value = [0, 2, 10, 6, 8, 12, 4]
# def func(x): return x % 2 == 0
#
# print(same_by(func, value))
#########################
def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == 0

value = [0, 2, 10, 6, 8, 12, 1]

if same_by(lambda x: x % 2, value):
    print('same')
else:
    print('different')

# 41) Напишите программу на Python для поиска пересечения двух
# заданных массивов с помощью Lambda, filter.

# a1 = [1,2,3,5,7,8,9,10]
# a2 = [1,2,4,8,9]
#
# new_lst = list(filter(lambda x: x in a2, a1))
# print(new_lst)
# print(sorted(set(a1).intersection(a2)))

# 2) Имеется упорядоченный список:

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной
# диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i, elem in enumerate(a):
#     a[i][i] = 0
#     print(*a[i])

# 43) Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с
# помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)
#
# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.
#
# Выведите имена сотрудников, получившие нечетные id.


# from random import randint
#
# ids = [randint(1, 100) for i in range(10)]
# names = ['Sergey', 'Olga', 'Roman', 'Evgeniy', 'Petr', 'Ivan', 'Konstantin', 'Maria', 'Sasha', 'Polina']
# lst = list(filter(lambda x: x[1] % 2, sorted(zip(names, ids), key=lambda x: x[1])))
# print(lst)


# Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers
# трехзначные числа, дающие при делении на 55 остаток 22, и выводит их кубы, каждый в отдельной строке.

# nums = [1, 2, 234, 5678, 654, 572, 132, 627]
#
# [print(i) for i in map(lambda x: x**3,
#                        filter(lambda x: len(str(x)) == 3 and x % 55 == 22, nums))]


#####################
# Отсортировать по средней цифре
# nums = [234, 568, 654, 572, 197]
# print(sorted(nums, key=lambda x: int(str(x)[1])))
##################

# a = ['safasfasff', 'aff', 'd', 'asfsaf']
# a = sorted(a, key=len)
# a1 = sorted(a, key=lambda x: len(x))
# print(a)
# print(a1)