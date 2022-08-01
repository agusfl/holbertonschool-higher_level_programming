#!/usr/bin/node
// Write a file that modifies the value of myVar to 333
/* Aca lo que se hace es redefinir a myVar (variable que esta definida en el archivo 100-main.js)
no le ponemos el let antes ya que si le pusieramos el let es como que estamos definiendo una nueva
variable en otro scope y no en el del archivo 100-main.js, esto va a tener errores de style porque
estas asignando valor a una variable que no definiste en este script, pero en la task dicen que no
nos preocupemos de el style de semistandar.
En el archivo de 100-main.js se llama con require a este archivo y se pasa lo que esta dentro de este
script para el script de 100-main.js, de esta forma se cambia el valor de myVar de 89 a 333. */

myVar = 333;
