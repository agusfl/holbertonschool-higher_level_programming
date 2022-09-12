#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer:

- The first argument is the movie ID
- You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
- You must use the module axios

Info axios: https://github.com/axios/axios
Info API star wars: https://swapi-api.hbtn.io/
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv
const axios = require('axios').default; // import axios module

const id = args[2];

// Usamos el modulo "axios" para hacer peticion GET del protocolo HTTP
// pasamos la ruta de la api de star wars con el numero de id que pasen como argumento en linea
axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error - para acceder al status del error, es atraves de la respuesta(response)
    console.log(`code: ${error.response.status}`);
  });
