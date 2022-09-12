#!/usr/bin/node
/*
Write a script that reads and prints the content of a file:

- The first argument is the file path
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv

const filePath = args[2];

const fs = require('fs'); // load fs class

fs.readFile(filePath, 'utf8', function (err, content) {
  if (err) {
    return console.log(err);
  }
  // Imprimo el contenido que leimos del archivo "file_path".
  console.log(content);
});
