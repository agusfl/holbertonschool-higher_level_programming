#!/usr/bin/node
// Write a function that executes x times a function.

// Defino la funcion callMeMoby que se llama en el archivo 101-main.js
const callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction(); // llamo a lafuncion que se pasa como segundo argumento.
  }
};
// exporto la funcion creada "callMeMoby" para que se pueda usar afuera de este script.
exports.callMeMoby = callMeMoby;
