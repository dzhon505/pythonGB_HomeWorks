# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


# str1 = 'a a a b c a a d c d d'
# symbol = str1.split()
# res = []
# for i in range(len(symbol)):
#     if symbol[i] in res:
#         res.append(symbol[i] + '_' + str(symbol[:i].count(symbol[i])))
#     else:
#         res.append(symbol[i])
# print(', '.join(res))



# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells " \
#        "that she sells are sea shells I'm sure.So if she sells sea" \
#        " shells on the sea shore I'm sure that the shells are sea" \
#        " shore shells"
# print(len(set(text.lower().split())))

# Задача №29.
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Ваня:
# n = int
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = n
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и востановления данных.
# Сжатие:
# 1112222334 -> 31322314
# aaabbbbbccd -> 3a3b2c1d
#
# Востановление:
# 31322414 -> 111222334
# 3a3b2c1d -> aaabbbbbccd




# доп*3.)
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input("Введите натуральное число: "))
list = []

