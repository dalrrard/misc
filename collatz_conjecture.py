__author__ = 'dalton'

def collatz(num):

    num = int(num)
    count = 0

    while num > 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num *= 3
            num += 1
            count += 1

    print(count)

collatz(input('Enter a number: '))