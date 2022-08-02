#!/usr/bin/node
// Write a script that concats 2 files.
/*
- The first argument is the file path of the first source file
- The second argument is the file path of the second source file
- The third argument is the file path of the destination
*/

const fs = require('fs'); // load fs class

fs.readFile('fileA', 'utf8', function (err, file) {
  if (err) {
    return console.log(err);
  }
  // Guardo lo que se leyo dentro del "file" (que seria el file A) dentro de una variable llamda "fileA"
  const fileA = file;
  // Uso la funcion "appendFile" de la clase "fs" para poder agregar (escribir) texto (el que leimos en fileA) dentro del archivo "fileC"
  fs.appendFile('fileC', fileA, function (err, f) {
    if (err) throw err;
  });
});

fs.readFile('fileB', 'utf8', function (err, file) {
  if (err) {
    return console.log(err);
  }
  // Guardo lo que se leyo dentro del "file" (que seria el file B) dentro de una variable llamda "fileB"
  const fileB = file;
  // Uso la funcion "appendFile" de la clase "fs" para poder agregar (escribir) texto (el que leimos en fileB) dentro del archivo "fileC"
  fs.appendFile('fileC', fileB, function (err, f) {
    if (err) throw err;
  });
});
