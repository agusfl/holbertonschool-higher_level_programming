// Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
// Lo que tenia de complicado esta tarea es que habia que ver hacia donde te rediriga la pagina
// inicial que era (https://fourtonfish.com/hellosalut/?lang=fr), pasamos un curl -k y con esto nos trae la pagina de la reedireccion
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data, status) {
  if (status === 'success') {
    $('DIV#hello').text(data.hello);
  }
});
