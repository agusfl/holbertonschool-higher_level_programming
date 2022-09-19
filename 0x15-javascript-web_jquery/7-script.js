// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// Info GET jquery: https://jquery-tutorial.net/ajax/the-get-and-post-methods/
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    // Si la respuesta fue exitosa (osea que se pudo traer la info con el metodo get)
    // traemos el nombre del personaje de starwars y lo mostramos en el DIV que tiene
    // el ID "character"
    $('#character').text(data.name);
  }
});
