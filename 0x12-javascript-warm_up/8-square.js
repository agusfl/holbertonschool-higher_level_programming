#!/usr/bin/node
// Script that prints a square
// repeat method --> https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/repeat

const process = require('process'); // agrego el modulo process usando "require" (se podria usar import tmb)
const args = process.argv; // defino args como process.argv asi uso args en el resto del codigo.
const size = args[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
