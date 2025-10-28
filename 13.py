# n = int(input())
# numbers = []
# for _ in range(n):
#     numbers.append(int(input()))
#
# for number in numbers:
#     if number < 0:
#         print(number , end=' ')


# names = ['Марат', 'Анна', 'Вася', 'Катя']
#
# # delete
# # del names[1]
# # print(names)
#
# names.remove('Вася')
# print(names)
#
#
books = ['Даниель Дефо -- Робинзон Крузо', 'Александр Пушкин -- Руслан и Людмила',
         'Жюль Верн -- Дети капитана Гранта', 'Лев Толстой -- Детство. Отрочество. Юность']

# print(0, books[0])
# print(1, books[1])
# print(2, books[2])
# print(3, books[3])
#
# for i in range(len(books)):
#     print(f'{i + 1}. {books[i]}')

books = ['Даниель Дефо -- Робинзон Крузо', 'Александр Пушкин -- Руслан и Людмила',
         'Жюль Верн -- Дети капитана Гранта', 'Лев Толстой -- Детство. Отрочество. Юность']

# numbers = [1, 2, 3]
# if 3 in numbers:
#     print('Есть')
# else:
#     print('Нет')

# if 'Дефо' in books:
#     print('Есть')
# else:
#     print('Нет')
#
# for i in range(len(books)):
#     if de in books[i]:
#         print(books[i])

# books = ['Даниель Дефо -- Робинзон Крузо', 'Александр Пушкин -- Руслан и Людмила',
#         'Жюль Верн -- Дети капитана Гранта', 'Лев Толстой -- Детство. Отрочество. Юность']
# my_books = []
# print('Добро пожаловать в библиотеку имени Ломоносова!')
# actions = ['Взять книгу напрокат', 'Сдать книгу', 'Найти книгу по фрагменту названия']
# act = 1
# while act != 0:
#    print('Список доступных действий: ')
#    for i in range(len(actions)):
#        print(f'{i + 1}. {actions[i]}')
#    act = int(input('Выберите действие: '))
#    if act == 1:
#        print('Список доступных на данный момент книг: ')
#        for i in range(len(books)):
#            print(f'{i}. {books[i]}')
#        num = int(input('Укажите номер книги, которую хотите взять напрокат: '))
#        print(f'{books[num]} - отличный выбор! Приятного чтения!')
#        my_books.append(books[num])
#        del books[num]
#        print()
#    if act == 2:
#        print('Ваши книги: ')
#        print(my_books)
#        index = int(input('Введите номер книги, которую хотите сдать или 100, если хотите сдать все'))
#        if index != 100:
#            books.append(my_books[index])
#        if index == 100:
#            books.extend(my_books)
#        print('Книга успешно сдана!')
#        print('Список доступных на данный момент книг: ')
#        for i in range(len(books)):
#            print(f'{i + 1}. {books[i]}')
#        print()
#    if act == 3:
#        line = input('Введите фрагмент названия: ')
#        print('Результаты поиска: ')
#        for name in books:
#            if line in name:
#                print(name)
#        print()
#
#
