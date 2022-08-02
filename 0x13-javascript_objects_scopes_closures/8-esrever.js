#!/usr/bin/node
// Write a function that returns the reversed version of a list

exports.esrever = function (list) {
  const newArray = []; // creamos un array vacio para guardar en reversa la lista que se pase en "list"
  const lastIndex = list.length - 1; // creo la variable lastIndex que va a ser el largo del array menos 1, porque sino accede a un espacio que no tenemos acceso.

  // Se hace un for para agregar los datos en el neuvo array en reversa.
  for (let i = lastIndex; i >= 0; i--) {
    newArray.push(list[i]); // uso el metodo push para agregar los datos en el array.
  }
  return newArray; // retornamos el nuevo array
};
