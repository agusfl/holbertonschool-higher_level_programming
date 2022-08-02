#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
/*
- Your script must import dict from the file 101-data.js
- In the new dictionary:
* A key is a number of occurrences
* A value is the list of user ids
- Print the new dictionary at the end
*/

// Importo el dict del archivo 101-data.js
const dict = require('./101-data.js').dict;
const newDic = {};
const array = [];

for (const key in dict) {
  // argego las "keys" al diccionario a retornar, que van a ser los valores del "dict" que nos pasan
  array.push(dict[key]);
}
// Nos quedamos con los valores unicos usando el objeto "Set" ponemos new (constructor) para crear una instancia (objeto) de Set.
const uniqueKeys = new Set(array);

// Se agregan las keys en el diccionario a retornar (newDic) y se le asigna un array vacio a cada key.
// Set se recorre con "of" a diferencia del array y el objeto que se recorre con "in".
for (const iter of uniqueKeys) {
  newDic[iter] = [];
}

for (const iter in dict) {
  const value = dict[iter];
  // agrego los valores dentro del nuevo diccionario, con el metodo push los agrego en la lista de cada "key" correspondiente.
  newDic[value].push(iter);
}

// imprimo el diccionario con los valores ordenados
console.log(newDic);
