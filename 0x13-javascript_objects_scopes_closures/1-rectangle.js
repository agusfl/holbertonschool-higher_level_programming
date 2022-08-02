#!/usr/bin/node
/*
You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
*/
// Aca se usa el constructor para definir las variables "w" y "h". Y despues se inicializan
// las variables que se cran "width" y "height" para cada objeto usando "this" con los valores
// que se pasen como argumento en "w" y "h".
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
