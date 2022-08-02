#!/usr/bin/node
// Create an instance method called print() that prints the rectangle using the character X

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  // add method "print()"
  print () {
    const rows = this.height;
    const columns = this.width;
    for (let i = 0; i < rows; i++) {
      console.log('X'.repeat(columns));
    }
  }
};
