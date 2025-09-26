# line = "ситуация непростая"
# Срезы
# print(line[2:5])
# print(line[0:8:2])
# print(line[::3])
# print(line[::-1])
# print(line[::-1])
from ctypes.wintypes import tagPOINT

# letters = 'a' * 100
# print(letters)

# Пользователь вводит строку
# Распечатать строку умноженную на 10
# a = input()
# print(a * 10)


# Пользователь вводит строку.
# Необходимо создать новую строку, такую же, но в середину вставлена буква а
# center = len(line) // 2

# ПользоAватель
# s = input()
# word = len(s) // 2 # 2
# print(s[:word] + "A" + s[word:])

# Циклы

# Цикл позволяет повторять какие-то действия сколько-то раз

# for i in [100, 1, 34, 56]:
#     print(i)


# 5, 8, 1, 90
# for i in (5, 8 , 1 ,90):
#     print(i)

# for letter in 'Marat':
#     print(letter)


# s = input()
# for i in s:
#     print(i)


# for i in range(10):
#     print(i)

# for i in range(501):
#     print(i)


# for i in range(10, 21):
#     print(i)


# a = int(input())
# b = int(input())
# for i in range(a,b + 1):
#     print(i)


# for i in range(1, 100, 2):
#     print(i)


# for i in range(0 , 101 , 5):
#     print(i)


# for i in range(10, 0, -1):
#     print(i)


# for i in range(1,11):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)
# print("ЗАПУСК")


# a = int(input())
# b = int(input())
# if a % 2 == 1:
#     a += 1
# for i in range(a, b + 1, 2):
#     print(i)

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i)

# Распечатать числа от а до б, которые делятся на 3
# a = int(input())
# b = int(input())
# for i in range(a,b + 1):
#     if i % 3 == 0:
#         print(i)

#
# a = int(input())
# b = int(input())
# if a % 3 == 1:
#     a += 2
# elif a % 3 == 2:
#     a += 1
# for i in range(a,b + 1, 3):
#     print(i)


# N = int(input())
# b = 0
# for i in range(10, 100):
#     if i // 10 == N or i % 10 == N:
#         b += i
#print(b)
# n = int(input())
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break
summ = 0
for i in range(25,56):
    summ += i * i * i
print(summ)
