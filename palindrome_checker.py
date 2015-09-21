__author__ = 'dalton'
import re

def palindrome(word):

    lower_word = word.lower().replace(' ', '')
    lower_word = re.sub(r'\W+', '', lower_word)

    if lower_word == lower_word[::-1]:
        print('"{}" is a palindrome'.format(word))
    else:
        print('"{}" is not a palindrome'.format(word))

palindrome(input('Enter a word or phrase: '))