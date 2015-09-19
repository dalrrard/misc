__author__ = 'dalton'
import math
import decimal
from sympy.mpmath import mp

def Pi():
    """precise to 15 places"""
    precision = int(input("How many decimal places would you like? "))
    context = decimal.Context(prec=precision+1)


    return context.create_decimal_from_float(2 * (math.asin(math.sqrt(1 - .5**2)) + abs(math.asin(.5))))

def PrecisePi():
    mp.dps = int(input("How many decimal places would you like? "))

    return mp.pi

print(PrecisePi())