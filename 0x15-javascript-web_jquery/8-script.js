// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// Info GET jquery: https://jquery-tutorial.net/ajax/the-get-and-post-methods/
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    // Si la respuesta fue exitosa (osea que se pudo traer la info con el metodo get)
    // traemos el nombre del personaje de starwars y lo mostramos en el DIV que tiene
    // el ID "character"
    const movies = data.results;
    for (const i in movies) {
      $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
    }
  }
});
