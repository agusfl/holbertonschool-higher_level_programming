#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    ld = number % 10
    print(ld, end='')
    return ld

# Se pasa el number a positivo ya que hay que imprimirlo sin el signo negatvio y no uso format en el print para que no
# haya lio con el checker ya que todavia no terminaron de arreglar el tema de f-string y .format.
