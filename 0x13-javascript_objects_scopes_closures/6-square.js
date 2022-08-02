#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
/*
- You must use the class notation for defining your class and extends
- Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
*/
// Importamos la clase Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // la clase Rectangle recibe 2 parametros, por eso le paso dos veces "size"
    this.size = size;
  }

  // add method "charPrint(c)"
  charPrint (c = 'X') { // seteo 'X' como valor default si no se pasa nada como argumento.
    for (let i = 0; i < this.size; i++) { // se puede usar tanto "height" como "width" - es un metodo de la class Rectangle por eso no usamos "size".
      console.log(c.repeat(this.size));
    }
  }
}

// Se exporta el modulo para que se pueda usar por los demas scripts (el script 6-main.js)
module.exports = Square;
