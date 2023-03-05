# Функции
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
#
# print(sum_numbers(5))
import random


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
#
# print(sum_str('q', 'e', 'r'))

# Модули
# from modul import max1
# print(max1(5, 9))

# import modul
# print(modul.max1(5, 9))


# import modul as m1
# print(m1.max1(5, 9))

# Рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)



# Сортировка


# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
#
# print(quick_sort([5,6,34,352,65,2342,2,97,67]))

# Сортировка слиянием


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,4,6,23,12,56,34,68,34]
merge_sort(list1)
print(list1)