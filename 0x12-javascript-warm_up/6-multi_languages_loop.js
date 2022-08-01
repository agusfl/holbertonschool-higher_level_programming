#!/usr/bin/node
// Script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop.
// Info: https://www.w3schools.com/js/js_loop_for.asp

const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let cont = 0; cont < array.length; cont++) {
  console.log(array[cont]);
}
