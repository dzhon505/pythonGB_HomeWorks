# def calk1(a,b):
#     return a+b
#
# def calk2(a,b):
#     return a*b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk2, 5, 4)

# def calk1(a,b):
#     return a+b
# calk1 = lambda a, b: a + b
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk1, 6, 45)

###############################
# def math(op, x, y):
#     print(op(x, y))
# math(lambda a,b: a + b, 5 ,41)
#################################


# data = [1,2,3,4,5,8,15,23,38]
# res = []
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
#
# print(res)
##################################

# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1,2,3,4,5,8,15,23,38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

###################################

# list1 = [i for i in range(10)]
# print(list1)
# list1 = list(map(lambda x: x+10, list1))
# print(list1)

####################################

# data = '15 156 96 3 5 8 52 5'
# print(data)
#
# data = list(map(int, data.split()))
# print(data)

#####################################

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

######################################

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

####################################

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)

##################################

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

###################################

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # a - открытие для добавления + создание, r - открытие для чтения, w - открытие для записи + создание,
# data.writelines(colors)   # w+ - Позволяет открывать для записи и читать из него + создание
# data.close()              # r+ - Позволяет открывать файл для чтения и дописывать в него.

##################################

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
#
# print(56)

#####################################

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

#######################################

