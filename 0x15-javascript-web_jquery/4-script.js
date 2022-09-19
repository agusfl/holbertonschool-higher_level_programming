// Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
// Info Toggle classes: https://www.w3schools.com/jquery/html_toggleclass.asp
// "Toggle" significa "alternar"
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#toggle_header');
  button.click(function () {
    $('header').toggleClass('red green');
  });
});
