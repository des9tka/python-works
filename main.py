# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.s = 1
#
#     def area(self):
#         self.s = self.x * self.y
#
#     def __add__(self, other):
#         return self.s + other.s
#
#     def __sub__(self, other):
#         return self.s - other.s
#
#     def __eq__(self, other):
#         return self.s == other.s
#
#     def __ne__(self, other):
#         return self.s != other.s
#
#     def __lt__(self, other):
#         return self.s < other.s
#
#     def __gt__(self, other):
#         return self.s > other.s
#
#     def __len__(self):
#         return self.x + self.y
#
# r1 = Rectangle(5,5)
# r2 = Rectangle(3,3)
# r1.area()
# r2.area()
# print(r1 + r2)
# print(r1 - r2)
# print(r1 == r2)
# print(r1 != r2)
# print(r1 < r2)
# print(r1 > r2)
# print(len(r1))
#   ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#
#     def search_cinderella(self, *other):
#         for i in other:
#             if self.shoe_size == i.foot_size:
#                 print(i.name)
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.count += 1
#
#     @classmethod
#     def show_count(cls):
#         return Cinderella.count
#
# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#
#     @abstractmethod
#     def print(self):
#         pass
#

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# class Book(Printable):
#
#     def __init__(self, name):
#         self.name = name
#
#     def print(self):
#         print(self.name)
#
#
# class Magazine(Printable):
#
#     def __init__(self, name):
#         self.name = name
#
#     def print(self):
#         print(self.name)
#

# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# class Main:
#     printable_list = []
#
#     @classmethod
#     def add(cls, other):
#         if isinstance(other, (Book, Magazine)):
#             cls.printable_list.append(other)
#
#     @classmethod
#     def show_all_magazines(cls):
#         for i in cls.printable_list:
#             if isinstance(i, Magazine):
#                 i.print()
#
#     @classmethod
#     def show_all_books(cls):
#         for i in cls.printable_list:
#             if isinstance(i, Book):
#                 i.print()

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
#
#
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта, __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
#
# l = []
#
#
# class Letter:
#     __count = 0
#
#     def __init__(self):
#         Letter.__count += 1
#         self.__text = ''
#
#     @classmethod
#     def show_count(cls):
#         print(cls.__count)
#
#     def set_text_to_list(self):
#         l.append(self.__text)
#
#     def get_text(self):
#         return self.__text
#
#     def set_text(self, text):
#         self.__text = text