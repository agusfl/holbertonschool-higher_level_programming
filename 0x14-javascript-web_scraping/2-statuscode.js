#!/usr/bin/node
/*
Write a script that display the status code of a GET request:

- The first argument is the URL to request (GET)
- The status code must be printed like this: code: <status code>
- You must use the module axios

Info axios: https://github.com/axios/axios
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv
const axios = require('axios').default; // import axios module

const URL = args[2];

// Usamos el modulo "axios" para hacer peticion GET del protocolo HTTP
axios.get(URL)
  .then(function (response) {
    // handle success
    console.log(`code: ${response.status}`);
  })
  .catch(function (error) {
    // handle error - para acceder al status del error, es atraves de la respuesta(response)
    console.log(`code: ${error.response.status}`);
  });
