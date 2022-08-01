#!/usr/bin/node
// Script that computes and prints a factorial

const process = require('process'); // agrego el modulo process usando "require" (se podria usar import tmb)
const args = process.argv; // defino args como process.argv asi uso args en el resto del codigo.
const num = parseInt(args[2]);

function factorial (num) {
  // if number is 0 or NaN (Not a Number) --> exit of recursion
  if (num === 0 || isNaN(num)) {
    return 1;
  } else { // Call recursive function
    return num * factorial(num - 1);
  }
}
// Hacemos un print con console.log del resultado de llamar a la funcion factorial que creamos recien.
console.log(factorial(num));
