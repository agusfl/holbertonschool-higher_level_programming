#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id:

- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
- Only print users with completed task
- You must use the module axios

Info axios: https://github.com/axios/axios
Info API json placeholder: https://jsonplaceholder.typicode.com/todos
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
    // Guardo la info que este en la pagina:
    const data = response.data;
    const dicResponse = {};

    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        // Si el "userId" tiene la tarea marcada como true en completed y ya esta dentro del diccionario que creamos sumamos 1
        if (dicResponse[data[i].userId] !== undefined) {
          dicResponse[data[i].userId] = dicResponse[data[i].userId] += 1;
          // En caso de que el "userId" tiene una tarea completa y no estaba en el diccionario se viene a este else y se le setea en uno, ya que es la primera vez que aparece
        } else {
          dicResponse[data[i].userId] = 1;
        }
      }
    }
    // Se retorna el diccionario con "userId" como "key" y la cantidad de tareas completadas como "value".
    console.log(dicResponse);
  })
  // No es necesario dejar el catch para el checker pero lo dejo como buena practica
  .catch(function (error) {
    // handle error - para acceder al status del error, es atraves de la respuesta(response)
    console.log(`code: ${error.response.status}`);
  });
