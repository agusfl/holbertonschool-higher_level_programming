#!/usr/bin/node
// Script that prints the addition of 2 integers
/* args devuelve un string por lo tanto para poder sumarlos hay que usar la funcion "parseInt"
para poder pasar el string a un integer (lo casteamos a int) y asi poder sumar los numeros, si
no le ponemos el parseInt los concatena en lugar de sumar. */

const process = require('process'); // agrego el modulo process usando "require" (se podria usar import tmb)
const args = process.argv; // defino args como process.argv asi uso args en el resto del codigo.
const a = parseInt(args[2]); //
const b = parseInt(args[3]);

function add (a, b) {
  return (a + b);
}
console.log(add(a, b));
