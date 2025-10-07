# i = 5
# while i != 0:
#     print(i)
#     i -= 1


# Пользователь вводит числа до тех пор, пока не введет 0
# 10
# 9
# 8
# 7
# 5
# 10
# 9
# 7
# 10
# 0

# a = int(input())
# while a != 0:
#     print(a)
#     a = int(input())


# Компьютер загадывает число, а пользователь угадывает его.

# Вложенные циклы

# 0 ч 0 мин
# 0 ч 1 мин
# 0 ч 2 мин
# 0 ч 3 мин
# ...
# 0 ч 59 мин
# 1 ч 0 мин
# 1 ч 1 мин
# 1 ч 2 мин
# ...
# 1 x 59 мин
# 23 ч 59 мин

# for hour in range(0, 24):
#     for minute in range(0, 60):
#         print(f'{hour} ч {minute} мин')


# for i in range(1,5):
#     for km in range(1,4):
#         print(f"{i} Круг {km} км")
#
#
# kmm = 0
# k = 0
# while k != 4:
#     print(f"{k} Круг {kmm} км")
#     kmm+=1
#     if kmm == 4:
#         kmm = 0
#         k+= 1

# Распечатать
# 1 2 3


# c = 3
# for j in range(4):
#     for i in range(1,c + 1):
#         print(i,end = " ")
#     print()


# 1 - 9

i = 1
# 1 * 1 = 1
# 1 * 2 = 1
# 1 * 3 = 1
# 1 * 4 = 1
# 1 * 5 = 1
# 1 * 6 = 1
# 1 * 7 = 1
# 1 * 8 = 1
# 1 * 9 = 1

# 2 * 1 = 1
# 2 * 2 = 1
# 2 * 3 = 1
# 2 * 4 = 1
# 2 * 5 = 1
# 2 * 6 = 1
# 2 * 7 = 1
# 2 * 8 = 1
# 2 * 9 = 1
# for i in range(1,10):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")
#     print()

# i = 1
# while i < 10:
#     j = 1
#     while j < 11:
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     i += 1


# name1 = 'Петя1'
# name2 = 'Петя2'
# name3 = 'Петя3'
# name4 = 'Петя4'
# name5 = 'Петя5'
# name6 = 'Петя6'
#
# print(name1)
# print(name2)
# print(name3)
# print(name4)

# Список
names = ['Марат', 'Петя', 'Ваня','Катя', 'Алиса']
# print(*names)

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# for i in range(5):
#     print(names[i])






# Предметы
items = ["Math","English","History"]
print(*items)

for i in range(3):
    print(items[i])