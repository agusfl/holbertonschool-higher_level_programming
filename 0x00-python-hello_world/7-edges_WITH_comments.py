#!/usr/bin/python3
word = "Holberton"
# Se crean 3 variables para hacer con el "slicing" los "cortes" que se quieren para imprimir la cantidad de letras
# que se nos pide en la letra.
word_first_3 = word[:3]
word_last_2 = word[7:9]
middle_word = word[1:8]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
