__author__ = 'dalton'


def fib(num):
    a = 0
    b = 1

    for i in range(num):
        print(a)
        a, b = b, a+b

num = fib(int(input('How many iterations? ')))