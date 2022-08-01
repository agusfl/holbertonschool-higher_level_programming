#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed
// Info: https://www.geeksforgeeks.org/node-js-process-argv-property/

const process = require('process'); // agrego el modulo process
const args = process.argv; // defino args como process.argv

if (args.length <= 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
