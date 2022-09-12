#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file:

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- You must use the module axios

Info axios: https://github.com/axios/axios
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv
const axios = require('axios').default; // import axios module

const URL = args[2];
const fileResponse = args[3]; // Archivo donde se va a escribir las respuesta con el contenido de la pagina
const fs = require('fs'); // load fs class

// Usamos el modulo "axios" para hacer peticion GET del protocolo HTTP
axios.get(URL)
  .then(function (response) {
    // handle success
    // Guardo la info que este en la pagina:
    const data = response.data;

    // Escribimos en el nombre que se pase para "fileResponse" el contenido de la pagina que se paso como primer argumento y guardamos en "URL"
    fs.writeFile(fileResponse, data, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  // No es necesario dejar el catch para el checker pero lo dejo como buena practica
  .catch(function (error) {
    // handle error - para acceder al status del error, es atraves de la respuesta(response)
    console.log(`code: ${error.response.status}`);
  });
