#!/usr/bin/python3
"""
Module 5-text_indentation, this module has a function that prints
a text with 2 new lines after each of the following characters: . ? :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after the following
    characters: . ? :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        characters = [".", ":", "?"]
        new_text = ""
        for element in text:
            new_text += element
            if element in characters:
                new_text += "\n"
                print(new_text.strip(" "))
                new_text = ""
        print(new_text.strip(" "), end="")
