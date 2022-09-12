#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name by line
- You must use the Star wars API
- You must use the module axios

Info axios: https://github.com/axios/axios
Info API star wars: https://swapi-api.hbtn.io/
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv
const axios = require('axios').default; // import axios module

const id = args[2]; // movie to search

// Usamos el modulo "axios" para hacer peticion GET del protocolo HTTP, pasamos la "id" como parametro
axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then(response => {
    for (const character in response.data.characters) {
    // Hacemos un GET request para cada personaje (character)
      axios.get(response.data.characters[character])
        .then(response => {
          // Imprimimos el nombre de lo que trae en el GET request de cada personaje
          console.log(response.data.name);
        });
    }
  })
  .catch(function (error) {
    // handle error - para acceder al status del error, es atraves de la respuesta(response)
    console.log(`code: ${error.response.status}`);
  });
