#!/usr/bin/node
// Script that prints two arguments passed to it, in the following format: “ is ”
/* En JavaScript cuando se quiere acceder a un espacio de memoria que no se tiene
permiso nos sale "undefined" en lugar de el error de segmentation fault que teniamos en
lenguajes como C. */

const process = require('process'); // agrego el modulo process
const args = process.argv; // defino args como process.argv

console.log(args[2] + ' is ' + args[3]);
// En el argumento 2 (que seria el 3) es donde va a estar la primer palabra que pongamos
// y en el arg 3 va a estar el segundo argumento que se ponga cuando se corra el programa.
