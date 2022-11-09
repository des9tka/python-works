# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
#
# st = 'as 23 fdfdg544'
# print(", ".join(i for i in st if i.isdigit()))

# #################################################################################

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# print(", ".join("".join([i if i.isdigit() else " " for i in st]).split()))

# #################################################################################

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# print(list(greeting.upper()))

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# numList = []
# for i in range(1, 50, 2):
#     numList.append(i**2)
#
# print(numList)

# function
# - створити функцію яка виводить ліст
# def listFunk(list):
#     print(list)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def mNum(a, b, c):
#    max1 = max(a, b, c)
#    print(max1)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def minMax(*args):
#     print(max(args))
#     return min(args)

# - створити функцію яка повертає найбільше число з ліста
# def mNum(list):
#     return max(list)

# - створити функцію яка повертає найменьше число з ліста
# def minNum(list):
#     return min(list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def sumDigit(list):
#     res = 0
#     for i in list:
#         res += i
#         return res

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def avg(list):
#     return sum(list)/len(list)

# ################################################################################################
# 1)Дан list:
list1 = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
def minN(list):
    print(min(list))

#   - видалити усі дублікати
def set_from_list(list):
    print(list(set(list1)))

#   - замінити кожне 4-те значення на 'X'
def swap(list):
    print(['X' if not (i + 1)%4 else v for i, v in enumerate(list)])
#
# swap(list1)
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def squer(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("*"*n)
        else:
            print("*" + " " * (n-2) + "*")

# 3) вывести табличку множення за допомогою цикла while
def multi_table() :
    i = 1
    while i <= 9:
        j= 1
        while j <= 9:
            res = i*j
            print(f'{res:4}', end='')
            j+= 1
        i+=1
        print()

# 4) переробити це завдання під меню
while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на "X"')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла')
    print('9) Exit')

    response = int(input('Choose: '))
    if response == 1:
        minN(list1)
    elif response == 2:
        set_from_list(list1)
    elif response == 3:
        swap(list1)
    elif response == 4:
        n = int(input('Choose the number: '))
        squer(n)
    elif response == 5:
        multi_table()
    elif response == 9:
        break
