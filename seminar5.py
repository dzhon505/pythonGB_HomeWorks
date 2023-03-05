# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


########### Рекурсия
# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input())
# print(fib(n))

# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def make_journal(x):
# #    journal = [int(input()) for i in range(x)] ###### List comprehnsion 4 нижние строки строки
#     # journal = []
#     # for i in range(x):
#     #     mark = int(input())
#     #     journal.append(mark)
#     return journal
#
# def swap_mark(lst):
#     maxx = max(lst)
#     minn = min(lst)
#     for i in range(len(lst)):
#         if lst[i] == maxx:
#             lst[i] = minn
#     return lst
#
#
# n = int(input())
# # new_journal = swap_mark(make_journal(n)) ##### Укороченная запись 2-х нижних строк
# lst_class = make_journal(n)
# new_journal = swap_mark(lst_class)
# print(new_journal)



# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# def check_simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return 'no'
#         return 'yes'
#
# n = int(input("Введите число: "))
# print(check_simple(n))



# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def rev(n):
#     x = int(input())
#     if n != 1:
#         rev(n - 1)
#     print(x, end = ' ')
#
# n = int(input('Введите количество чисел: '))
# rev(n)