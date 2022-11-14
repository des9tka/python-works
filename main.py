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
