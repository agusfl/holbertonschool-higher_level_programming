#!/usr/bin/node
/*
- You must use the class notation for defining your class
- The constructor must take 2 arguments w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
*/
// Se pone la condicion de que si 'w' o 'h' son menor o igual a 0 se retorne (el return vacio crea
// un objeto vacio) y tmb se agrega la condicion de que si 'h' o 'w' son "undefined" ya que por ejemplo
// en el caso de 'r3' del 2-main.js se pasa solo un valor --> 2 y el otro como no lo pasan es "undefined".

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
