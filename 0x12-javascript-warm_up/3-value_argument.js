#!/usr/bin/node
// Script that prints the first argument passed to it.

/* Si no existe el argumento 2 que es el primer argumento que se toma despues de
imprimir el path y el nombre del programa, indico que se imprima 'No Argument' tal
cual lo pide la letra y si existe en el else le indico que se imprima el nombre del
argumento que se pase. */

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
