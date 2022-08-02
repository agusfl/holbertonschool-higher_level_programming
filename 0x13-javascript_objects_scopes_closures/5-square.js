#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
/*
- You must use the class notation for defining your class and extends
- The constructor must take 1 argument: size
- The constructor of Rectangle must be called (by using super())
*/
// Use of extends: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends
// Use of super: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // la clase Rectangle recibe 2 parametros, por eso le paso dos veces "size"
  }
}

module.exports = Square;
