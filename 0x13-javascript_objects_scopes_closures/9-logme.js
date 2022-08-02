#!/usr/bin/node
// Write a function that prints the number of arguments already printed and the new argument value

// declaro una variable global para usar como contador e incrementarla cada vez que se llama a la funcion.
let cont = 0;

exports.logMe = function (item) {
  console.log(cont + ': ' + item); // imprimo en el formato que nos piden en la letra del ej.
  cont++; // incremento el contador cada vez que se llame a la funcion.
};
