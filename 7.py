# n = int(input())
# i = int(input())
# a = i // 100
# b = i // 10 % 10
# c = i % 10
# d = a + b + c
# if d == n:
#     print("yes")
# else:
#     print("no")

# n = int(input())
# b = 0
# for i in range(100, 1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     d = a + b + c
#     if d == n:
#         b+=1
# print(b)

# age = int(input())
# Сейчас вам <age> лет, через 5 лет Вам будет <> лет
# print("Сейчас вам", age, "лет, через 5 лет Вам будет",age + 5,"лет")
# print(f"Сейчас вам {age} лет, через 5 лет Вам будет {age + 5} лет")

# Пользователь вводит текущее кол-во
# рублей в копилке и сколько он положит в копилку завтра

# 100
# 50
# 150
# a = int(input())
# b = int(input())
# print(f"Сейчас у вас в копилке {a} денег завтра у вас будет в копилке {a + b} денег")


# Трекер устного счета
# 20 + 12 = 32
# Правильно!
# 10 + 45 = 67
# Неправильно
# ...
# Правильных ответов: 3
# Вердикт: Вы неплохо считаете

# import random
# from random import randint, choice
# operators = ['+', '-']
# # random - случайный
# # int - integer - целое число
# num = 0
# for i in range(1, 6):
#     a = randint(10, 999)
#     b = randint(10, 999)
#     op = choice(operators)
#
#     c = int(input(f"{i}. {a} + {b} = "))
#     if c == a + b:
#         print("Правильно!")
#         num+=1
#     else:
#         print("Неправильно")
# print(f"Вы набрали {num} балов")
# if num <= 1:
#     print("Вердикт:Вы плохо считаете")
# elif num <= 3:
#     print("Вердикт: Вы неплохо считаете")
# elif num == 4:
#     print("Вердикт: Вы хорошо считаете")
# elif num == 5:
#     print("Вердикт: Вы отлично считаете")

# operators = ['+', '-']
# op = choice(operators)
# a = 10
# b = 34
# if op == '+':
#     res = a + b
# else:
#     res = a - b
#
# res = a + b if op == '+' else a - b


# choice - выбор


# from random import randint, choice
#
# operators = ['+', '-']
# num = 0
# for i in range(1, 6):
#     a = randint(10, 999)
#     b = randint(10, 999)
#     op = choice(operators)
#     c = int(input(f"{i}. {a} {op} {b} = "))
#     if op == '+':
#         if c == a + b:
#             print("Правильно!")
#             num += 1
#         else:
#             print("Неправильно")
#             num += 1
#     if op == '-':
#         if c == a - b:
#             print("Правильно")
#             num += 1
#         else:
#             print("Неправильно")
# print(f"Вы набрали {num} балов")
# if num <= 1:
#     print("Вердикт:Вы плохо считаете")
# elif num <= 3:
#     print("Вердикт: Вы неплохо считаете")
# elif num == 4:
#     print("Вердикт: Вы хорошо считаете")
# elif num == 5:
#     print("Вердикт: Вы отлично считаете")
# a = randint(10, 999)
#     b = randint(10, 999)
#     op = choice(operators)
#     c = int(input(f"{i}. {a} {op} {b} = "))
# op = '+'
# if op == '+' and c == a + b:
#     print("Правильно!")
#     num += 1
# elif op == '-' and c == a - b:
#     print("Правильно")
#     num += 1
# else:
#     print('Неправильно')
