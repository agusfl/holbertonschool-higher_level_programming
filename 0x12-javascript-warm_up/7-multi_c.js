#!/usr/bin/node
// Script that prints x times “C is fun”

const process = require('process'); // agrego el modulo process usando "require" (se podria usar import tmb)
const args = process.argv; // defino args como process.argv asi uso args en el resto del codigo.

if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}
