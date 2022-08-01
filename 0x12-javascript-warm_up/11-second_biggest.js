#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.

const process = require('process'); // agrego el modulo process usando "require" (se podria usar import tmb)
const args = process.argv; // defino args como process.argv asi uso args en el resto del codigo.
let array = [];

if (!args[2]) {
  console.log('0');
} else if (args.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < args.length; i++) {
    array.push(parseInt(args[i]));
    array.sort();
	array = [...new Set(array)];
  }
  console.log(array[array.length - 2]);
}
