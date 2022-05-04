#!/usr/bin/python3

"""
Function that returns the weigthed average of all integers
tuple (<score>, <weigth>).
"""


def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        numerador = 0
        denominador = 0
        for i in my_list:
            numerador += i[0] * i[1]
            denominador += i[1]
        return (numerador / denominador)
