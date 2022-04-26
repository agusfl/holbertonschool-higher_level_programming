#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    ld = number % 10
    print(ld, end='')
    return ld
