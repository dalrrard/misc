__author__ = 'dalton'
import math


def prime(num):

    dictionary = {i: True for i in range(2, num+1)}

    for i in range(2, int(math.sqrt(num)+1)):
        if dictionary[i]:
            for j in range(num+1):
                x = (i**2) + (j*i)
                dictionary[x] = False


    answer = [x for x in dictionary if dictionary[x] == True]

    for i in answer:
        if num % i == 0:
            print(i)


prime(int(input('Get factors of which number? ')))