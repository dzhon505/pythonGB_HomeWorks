# Задача №1. Общее обсуждение
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
# import math

# n = int(input("Введите сколько километров в день: "))
# m = int(input("Введите сколько всего проехала машина: "))
# print("Количество дней: ", math.ceil(m / n))


# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# numClass = int(input("Введите количество классов: "))
# count = 0
# sum = 0
# while count < numClass:
#     clas = int(input("Введите количество учеников в классе: "))
#     part = math.ceil(clas / 2)
#     sum += part
#     count += 1
# print("Нужно парт: ", sum)

# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input("Номер вагона от головы: "))
# j = int(input("Номер вагона в который сел: "))
# if i == j:
#     print("Мало данных!")
# else:
#     print(i + j - 1)

# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

y = int(input("Введите год: "))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("YES")
else:
    print("NO")
