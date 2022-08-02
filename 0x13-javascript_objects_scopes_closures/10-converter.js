#!/usr/bin/node
// Write a function that converts a number from base 10 to another base passed as argument.
/*
- Prototype: exports.converter = function (base)
- You are not allowed to import any file
- You are not allowed to declare any new variable (var, let, etc..)
*/
// toString() method --> https://javascript.plainenglish.io/number-base-conversion-in-javascript-8bc44219b4ab

exports.converter = function (base) {
  function numReturn (num) {
    return num.toString(base);
  }
  return (numReturn);
};

/*
Usamos el metodo toString que lo que hace es convertir de base 10 a otras bases.
En la letra se nos indica que no podemos crear nuevas variables, por lo tanto lo que hago es crear una
funcion dentro de la funcion "converter" que estamos creando y en esa funcion que creo adentro ("numReturn")
le indico que va a recibir una variable llamada "num" y a esta le aplico el metodo "toString", por ultimo retorno
la funcion "numReturn".
*/
