#!/usr/bin/node
/*
Write a script that writes a string to a file:

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in utf-8
- If an error occurred during while writing, print the error object

Info write a file: https://nodejs.dev/en/learn/writing-files-with-nodejs/
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv

const filePath = args[2]; // archivo donde se va a escribir el contenido
const content = args[3]; // contenido a escribir

const fs = require('fs'); // load fs class

fs.writeFile(filePath, content, err => {
  if (err) {
    console.error(err);
  }
});
