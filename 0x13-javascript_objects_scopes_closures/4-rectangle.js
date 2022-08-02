#!/usr/bin/node
/*
Create an instance method called rotate() that exchanges the width and the height of the rectangle
Create an instance method called double() that multiples the width and the height of the rectangle by 2
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  // add instance method "print()"
  print () {
    const rows = this.height;
    const columns = this.width;
    for (let i = 0; i < rows; i++) {
      console.log('X'.repeat(columns));
    }
  }

  // add instance method "rotate()"
  rotate () {
    const pivot = this.width; // creamos la variable "pivot" para no perder el valor de la variable y poder hacer el cambio.
    // intercambiamos los valores de height por width:
    this.width = this.height;
    this.height = pivot;
  }

  // add instance method "double()"
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
