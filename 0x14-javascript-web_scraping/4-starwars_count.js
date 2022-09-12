#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present:

- The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
- You must use the module axios

Info axios: https://github.com/axios/axios
Info API star wars: https://swapi-api.hbtn.io/
*/

// process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
const process = require('process'); // agrego el modulo process para usar la funcion "argv".
const args = process.argv; // defino args como process.argv
const axios = require('axios').default; // import axios module

const URL = args[2];
// Le paso toda la ruta como texto y el 18 alfinal (la "id") para que sea comparable en el if
const id = 'https://swapi-api.hbtn.io/api/people/18/'; // esta es la id del actor que tenemos que filtrar

// Usamos el modulo "axios" para hacer peticion GET del protocolo HTTP
axios.get(URL)
  .then(function (response) {
    // handle success
    // Guardo todas las peliculas:
    const movies = response.data.results;
    let cont = 0; // creamos varaible para contar cuantas veces aparece el actor con id 18

    // Recorremos los characteres de cada pelicula
    for (let i = 0; i < movies.length; i++) {
      for (let j = 0; j < movies[i].characters.length; j++) {
        if (movies[i].characters[j] === id) {
          cont++; // Se aumenta el contador cada vez que se encuentre la id 18 en alguna pelicula.
          break; // Se hace un break para que no siga recorriendo la misma pelicula una vez que encotnro la id
        }
      }
    }
    console.log(cont);
  })
