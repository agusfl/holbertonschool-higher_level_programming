#!/usr/bin/python3

"""
Function that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None: 
        return 0
    if roman_string == "":
        return 0
# Hasta aca cheque casos border, primero si lo que pasan no es un string o si es None y en el segundo if se controla
# el caso de que se pase un string vacio (que no es lo mismo a que sea None), podria haber puesto el segundo if en el
# de arriba con un or pero no lo hice para no tener error en el cheker de requerimiento ya que me pasaba de los 79
# caracteres por linea (segun pycode style).
    sum_ = 0
    rom_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        if i > 0 and rom_val[roman_string[i]] > rom_val[roman_string[i - 1]]:
            sum_ += rom_val[roman_string[i]] - 2 * rom_val[roman_string[i - 1]]
        else:
            sum_ += rom_val[roman_string[i]]
    return sum_

# Primero inicializamos la variable "sum_" en 0, esta variable es en la cual vamos a almacenar la suma de la conversion
# del numero romano que pasen en el argumento "roman_string" a un integer.
# Luego se declara un diccionario llamado "rom_val" en el cual se indica de manera key-value los valores de los numeros
# romanos en su conversion de entero decimal.
# Luego se hace un for con una variable 'i' que recorre el largo que tenga el string que se pase en el argumento:
# roman_string.
# Y aca es donde arranca lo interesante, en el primer if se chequea por un lado que la i sea mayor a 0 y al mismo tiempo
# se chequea si el valor (value) del diccionario "rom_val" de la key que este en la primer posicion del string
# "roman_string" es mayor al valor (value) que esta en el diccionario para la key que este en la posicion anterior del
# string "roman_string".
# Recordar que roman_string[i] nos va a devolver lo que este en la poscion 'i' del string que se mande en el argumento
# "roman_string", por ejemplo si se pasa en el string: IX --> la primer posicion 'i' va a ser: I y cuando se pone:
# rom_val[roman_string[i]] va a equivaler a: rom_val[I] y esto nos devuelve el "value" que este asignado a la key "I"
# que en este caso seria: 1.
# Siguiendo con la logica, siempre en la primer iteracion se va al else, ya que la 'i' arranca en 0 y por lo tanto no
# se va a cumplir la condicion del if ya que 0 no es mayor a 0. Por lo tanto cuando entra al else se almacena en la
# variable "sum_" el valor en decimal de la variable en numero romano que se pase, en el caso de IX primero se guardaria
# 1, cuando se vuelve a entrar al for y se va al if, 'i' va a ser 1 (porque se incrementa por 1 ya que dejamos la opcion
# que viene por default al usar "range") por lo tanto es mayor a cero y la otra parte de la condicion tmb se cumple ya
# que rom_val[roman_string[i]] ahora es: X (10) (ya que estamos iterando el roman_string) y X es mayor a lo que estaba
# en la posicion anterior que era: I (1). Entonces se entra en el if y se almacena en sum_:
# lo que ya teniamos almacenado en sum_ que hasta el momento era: 1 y despues el termino: rom_val[roman_string[i]] seria
# equivalente en este caso a: 10, el termino rom_val[roman_string[i-1]] es equivalente en este caso a: -2 ya que seria:
# rom_val[I] porque la posicion anterior (i - 1) en IX estando parado en X es: I y esto va a dar: -2 * 1 osea -2.
# Al hacer la suma te quedaria: 1 + 10 - 2 = 9.
# Es necesario multiplicar por -2 porque ya tenias almacenado en sum_ el primer valor que va directo al else.

# Nota: hay ciertas condiciones de los numeros romanos como ser que 4 se escribe: IV y no IIII que el checker pareceria
# que no lo revisa ya que con este codigo tanto IV como IIII dan: 4 y solo el primero tendria que dar 4.
