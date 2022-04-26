#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

# Este es el main que nos pasaron de holberton, en python para probar los codigos con main, hay que darle permisos
# de ejecucion al main y ejecutarlo nomas ya que este va a llamar con el __import__('7-islower') llaman a tu programa
# que en este caso tiene nuestra funcion 'islower' que creamos.
