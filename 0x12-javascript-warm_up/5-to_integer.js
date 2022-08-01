#!/usr/bin/node
// Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
// isNan --> https://www.w3schools.com/jsref/jsref_isnan_number.asp#:~:text=In%20JavaScript%2C%20NaN%20is%20short,the%20type%20is%20a%20Number.

const process = require('process'); // agrego el modulo process usando "require" (se podria usar import tmb)
const args = process.argv; // defino args como process.argv asi uso args en el resto del codigo.

if (isNaN(args[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[2]);
}
