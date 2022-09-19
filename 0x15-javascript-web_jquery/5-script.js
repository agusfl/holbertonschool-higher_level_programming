// Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:
// Info Toggle classes: https://www.w3schools.com/jquery/html_toggleclass.asp
// "Toggle" significa "alternar"
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#add_item');
  button.click(function () {
    $('ul.my_list').append($('<li>Item</li>'));
  });
});

/* Tambien se podria hacer asi sin definir variables ni nada:
$('DIV#add_item').click(function () {
  $('ul.my_list').append($('<li>Item</li>'));
});
*/
