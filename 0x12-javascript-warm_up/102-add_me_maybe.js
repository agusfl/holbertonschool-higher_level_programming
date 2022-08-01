#!/usr/bin/node
// Write a function that increments and calls a function.

// Defino la funcion addMeMaybe que se llama en el archivo 101-main.js
const addMeMaybe = function (number, theFunction) {
  const increment = number + 1; // hago el incremento del numero que se pase como argumento.
  theFunction(increment); // llamo a lafuncion que se pasa como segundo argumento.
};
  // exporto la funcion creada "addMeMaybe" para que se pueda usar afuera de este script.
exports.addMeMaybe = addMeMaybe;
