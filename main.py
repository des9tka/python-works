# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
# try:
#     with open('files/emails.txt') as file, open('files/gmail.com_emails', mode='r+') as new_file:
#         for item in file:
#             new = item.split()
#             for i in new:
#                 if 'gmail.com' in i:
#                     new_file.write(f'{i}\n')
#
# except Exception as err:
#     print(err)
#
#
# # 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
count = 1


def init():
    global count
    try:
        with open('files/purchases') as file:
            for line in file:
                last_line = line
            count = int(last_line[0])
            count += 1

    except Exception as err:
        print(err)


class Purchase:

    @classmethod
    def show_all_purchases(cls):
        try:
            with open('files/purchases', mode='r') as purchases:
                print(purchases.read())
        except Exception as err:
            print(err)

    @classmethod
    def add_purchase(cls, name, price):
        global count
        try:
            with open('files/purchases', mode='a') as purchases:
                purchases.write(f'{count}) {name} --- {price}\n')

        except Exception as err:
            print(err)

    @classmethod
    def find_purchase(cls, find_field):
        try:
            with open('files/purchases', mode='r') as purchases:
                for purchase in purchases:
                    split = purchase.split()
                    for i in split:
                        if i == find_field:
                            print(f'\n{purchase}')
        except Exception as err:
            print(err)

    @classmethod
    def del_purchase(cls, search_id):
        try:
            with open('files/purchases', mode='r+') as purchases:
                for purchase in purchases:
                    split = purchase.split()
                    for i in split:
                        if f'{search_id})' == i:
                            print('del')
        except Exception as err:
            print(err)

    @classmethod
    def find_ME_purchase(cls):
        try:
            with open('files/purchases', mode='r') as purchases:
                new_list = []
                for purchase in purchases:
                    purch = purchase.split()
                    new_list.append(int(purch[3]))

                Purchase.find_purchase(max(new_list))

        except Exception as err:
            print(err)


def Main():
    while True:
        init()
        try:
            print('\n1) Show all purchases')
            print('2) Add a purchase')
            print('3) Find a purchase')
            print('4) Find the most expensive purchase')
            print('5) Delete a purchase by ID')
            print('0) Exit\n')
            response = int(input('Choose a number: '))

            if response == 1:
                Purchase.show_all_purchases()
            elif response == 2:
                res1 = input('Input name: ')
                res2 = input('Input price: ')
                Purchase.add_purchase(res1, res2)
            elif response == 3:
                res = input('Input filter: ')
                Purchase.find_purchase(res)
            elif response == 4:
                Purchase.find_ME_purchase()
            elif response == 5:
                res = input('Input ID: ')
                Purchase.del_purchase(res)
            elif response == 0:
                res = input('Y/N?: ')
                res.upper()
                if 'Y' in res:
                    break
                elif 'N' in res:
                    continue

        except Exception as err:
            print(err)
            continue


Main()
