# import easygui
from easygui import msgbox, enterbox

# msgbox('Привет, я загадал для тебя слово')
# d = enterbox('Введите букву: ')
# message - сообщение
# box - коробка
# letters = ['*', '*', '*']
# msgbox(letters)

# join - присоединиться

# fruits = ['Яблоко', 'Банан','Апельсин']
# l = '       '.join(fruits)
# print(l)


# fruits = ['Яблоко', 'Банан','Апельсин']
#
# print(fruits)
#
# fruits.append('Слива')
# fruits.append('Слива')
# fruits.append('Слива')
# fruits.append('Слива')
# fruits.append('Слива')
#
# print(fruits)
n = int(input())
lst = []
for i in range(n):
    a = input()
    lst.append(a)


for i in range(n):
    if lst[i] == 'Марат':
        print(lst[i])

# if lst[0] == 'Марат':
#     print(lst[0])
# if lst[1] == 'Марат':
#     print(lst[1])
# if lst[1] == 'Марат':
#     print(lst[1])
