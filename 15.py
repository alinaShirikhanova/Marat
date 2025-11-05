
# def sum_digits(num):
#     s = 0
#     while num != 0:
#         s += num % 10
#         num //= 10
#
#     print(s)
#
#
# n = int(input())
# sum_digits(n)
#
# print(s)


def summa_numers(number):
    s = 0
    while number !=0:
        s+= number % 10
        number //= 10
    return s


n = int(input())
m = int(input())
sum_m = summa_numers(m)
sum_n = summa_numers(n)
if  sum_m > sum_n:
    print(sum_m)
else:
    print(sum_n)