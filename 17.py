# class Person:
#     def __init__(self, a, n):
#         self.age = a
#         self.name = n
#
#
# p1 = Person(10, 'Марат')
# print(p1.age)
# print(p1.name)
#
# p2 = Person(100, 'Алена')
# print(p2.age)

# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def hello(self):
#         print(f'Привет! Меня зовут {self.name} породы {self.breed}')




# c1 = Cat('Мурзик', 'Чеширский')
# c1.hello()
#
# c2 = Cat('Пушистик', 'Дворняга')
# c3 = Cat('Миша', 'Бенгальский')
# c3.hello()

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print(f'{self.name} бежит')
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def meow(self):
#         print()
#
#
# c1 = Cat('jsf')
# c1.run()
#
#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print(f'{self.name} бежит')


import pygame

pygame.init()

pygame.display.set_mode((500, 500))

while True:
    pass

