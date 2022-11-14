# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# def notebook():
#     todo_list = []
#
#     def add_new_todo(todo: str):
#         todo_list.append(todo)
#         return todo_list
#
#     def show_todo_list() -> None:
#         print(todo_list)
#
#     return [add_new_todo, show_todo_list]
#
# add_todo, show_todo = notebook()
# add_todo('do a homework')
# show_todo()
#
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# def expanded_form(num):
#     res = []
#     for item, index in enumerate(str(num)[::-1]):
#         if int(index) != 0:
#             res.append(index + ('0' * item))
#
#     return ' + '.join(res[::-1])
#
# print(expanded_form(123))
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій
# def counter(funk):
#     count = 0
#     def innit():
#         nonlocal count
#         count += 1
#         funk()
#         print(count)
#
#     return innit
#
# @counter
# def foo():
#     print('foo')
#
# foo()
# foo()
# foo()
# foo()
# foo()
#
#
# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
# def fibanachi(num: int) -> None:
#     prev = 0
#     next = 0
#     l = []
#     for i in range(num):
#         if next == 0:
#             next = prev + i
#             l.append(str(next))
#             prev = i
#         elif next != 0:
#             next, prev = prev, next
#             next = next + prev
#             l.append(str(next))
#
#     print(", ".join(l))
#
#
# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
# def counter(num: int) -> None:
#     n = str(num)
#     p = []
#     un_p = []
#     for i in n:
#         i = int(i)
#         if i%2 == 1:
#             un_p.append(i)
#         else:
#             p.append(i)
#
#     print(f'paired = {len(p)} \nunpaired = {len(un_p)}')
#
#
# прога, що виводить кількість кожного символа з введеної строки,
#   наприклад:
#   st = 'as 23 fdfdg544' #введена строка
#
#   'a' -> 1  #вивело в консолі
#   's' -> 1
#   ' ' -> 2
#   '2' -> 1
#   '3' -> 1
#   'f' -> 2
#   'd' -> 2
#   'g' -> 1
#   '5' -> 1
#   '4' -> 2
#
# def str_count(string: str) -> None:
#     set = []
#     for i in string:
#         if i not in set:
#             print(f'{i} -> {string.count(i)}')
#             set.append(i)
#
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
def l_foo(l: list) -> None:
    new_list = []
    items = []
    index = 1
    while len(l) != 0:
        items.append(l[:index])
        new_list.append(items)
        items = []
        index += 1
    print(new_list)

l_foo([1,3,5,7,9])

# найти со списка только уникальные числа
# пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]
#
# def uniq_digits(l: list):
#     new_list = []
#     for i in l:
#         item = l.count(i)
#         if item == 1:
#             new_list.append(i)
#
#     print(new_list)