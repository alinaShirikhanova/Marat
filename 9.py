# for i in range(0,10):
#     for j in range(0,10):
#         print(f"{i} {j}")


# lst = [1] * 5
# print(lst)
# Пользователь вводит число - из этого числа должен состоять

# 10
# 3
#
# 10 10 10
#
# from random import randint
#
# words = ['переменная', 'строка', 'список', 'цикл', 'программа']
# meanings = ['именованная область памяти, адрес которой можно использовать для получения или измнения данных',
#            'тип данных, значениями которого является произвольная последовательность символов алфавита',
#            'мультитипная упорядоченная изменяемая коллекция',
#            'многократное выполнение одних и тех же действий',
#            'последовательность инструкций, предназначенная для исполнения устройством управления вычислительной машины']
# num = randint(0, len(words))
# word = words[num]
# print(f'Привет! Я загадал слово из {len(word)} букв, попробуй его угадать!')
# print(f'Это - {meanings[num]}')
# tries = 5
# letters = ['*'] * len(word)
# while tries > 0 and '*' in letters:
#    print('Оставшиеся буквы:')
#    print(*letters)
#    guess = input('Введите вашу букву: ')
#    if guess in word:
#        count = word.count(guess)
#        for i in range(count):
#            ind = word.index(guess)
#            letters[ind] = guess
#            word = word[:ind] + '*' + word[ind + 1:]
#    else:
#        tries -= 1
#        print('Такой буквы нет!')
#        print(f'У вас осталось {tries} попыток')
# if tries != 0:
#    print(*letters)
#    print('Победа!')
# else:
#    print('Слово: ', *letters)
#    print('Вы проиграли')

#
#
#
#
# words = ['цикл', 'переменная', 'список']


# letters = ['*', 'ф', 'ф']
#
# if '*' in letters:
#     print('Звездочки еще есть')
# else:
#     print("звездочек нет")


# l1 = ['*' * 10]
# print(l1)
# l2 = ['*'] * 10
# print(l2)


# word = 'цикл'
# letters = ['*', '*', '*', '*']
#
# d = 'и'
# ind = word.index(d)
# print(ind)
#
# letters[1] = 'и'
#
# letters[ind] = d
# print(letters)


# Пользователь вводит слово и букву на разных букву. РАспечатать индекс ,
# под которым стоит введенная буква во введенном слове


# квитанция
# я
#
# 8
# d = input()
# f = input()
# if f in d:
#     print(d.index(f))


# lst = [1, 2, 3, 4, 5]
# h = int(input())
# hf = int(input())
# lst[h] = hf
# print(lst)
# Считать индекс и значение,
# которое нужно присвоить в ячейку под этим индексом

# 2
# 100







