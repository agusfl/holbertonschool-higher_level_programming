#!/usr/bin/python3

"""
Function that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    if roman_string == "":
        return 0
    sum_int = 0
    rom_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        if i > 0 and rom_val[roman_string[i]] > rom_val[roman_string[i - 1]]:
            sum_ += rom_val[roman_string[i]] - 2 * rom_val[roman_string[i - 1]]
        else:
            sum_ += rom_val[roman_string[i]]
    return sum_i
