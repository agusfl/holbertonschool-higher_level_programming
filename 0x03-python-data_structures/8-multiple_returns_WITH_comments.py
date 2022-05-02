#!/usr/bin/python3
"""
Function that returns a tuple with the length of a string and its first
character.
"""


def multiple_returns(sentence):
    if not sentence: # Si la sentence no existe que retorne una tupla con largo 0 y None ya que no va a tener primer
        # character.
        return (0, None)
    else:
        length = len(sentence) # Aca calulamos el largo de la "sentence". Este va a ser el primer elemento de la
        # tupla que vamos a crear para devovler en el return.
        first_letter = sentence[0] # Segundo elemento de la tupla, es el primer caracter que haya en "sentence".
        new_tuple = (length, first_letter)
        return new_tuple
