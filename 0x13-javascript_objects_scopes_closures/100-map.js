#!/usr/bin/node
// Write a script that imports an array and computes a new array.

// Importo la lista del archivo 100-data.js, con el .list le indico que quiero traer la lista.
const list = require('./100-data.js').list;
// Otra forma de importar seria con "desestructuracion" asi: const { list } = require('./100-data.js');
// de esta forma se puede indicar todos los elementos que se quieran importar del archivo 100-data.js.

// Use of map function --> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control
// "value" representa el valor de cada elemento del array y "idx" representa al indice de dicho elemento.
const newArray = list.map((value, idx) => value * idx);
console.log(list);
console.log(newArray);
