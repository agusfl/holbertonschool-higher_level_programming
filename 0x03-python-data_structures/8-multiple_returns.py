#!/usr/bin/python3
"""
Function that returns a tuple with the length of a string and its first
character.
"""


def multiple_returns(sentence):
    if sentence is None:
        return None
    else:
        length = len(sentence)
        first_letter = sentence[0]
        new_tuple = (length, first_letter)
        return new_tuple
