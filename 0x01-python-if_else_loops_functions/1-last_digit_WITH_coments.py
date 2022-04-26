#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = number % -10 # Creamos una variable ld (last digit) para almacenar el ultimo digito y si el numero es negativo
    # lo pasamos a positivo para que no nos de errores con el numero que agarra como ultimo digito.
else:
    ld = number % 10

if ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
elif ld < 6:
    print(f"Last digit of {number} is {ld} less than 6 and not 0")
else:
    print(f"Last digit of {number} is {ld} and is greater than 5")
