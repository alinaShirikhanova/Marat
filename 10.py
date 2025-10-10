word = 'инициализация'
letters = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
d = input('Введите букву: ')
if d in word:
    print('Верно!')
    n = word.count(d)

    word_list = list(word)
    for i in range(n):
        ind = word_list.index(d)
        letters[ind] = d
        word_list[ind] = '#'
        print(*letters)




    ind = word.index(d)
    letters[ind] = d
    print(*letters)


word = 'инициализация'
word_list = list(word)
word_list[0] = '#'
word_list.index('и')
# print(word.index('и'))
# word_list = list(word)
# print(word_list)
# print(word.index('и'))
# print(word.index('и'))
# print(word.index('и'))
# print(word.index('и'))


# n = word.count('и')
# print(n)
