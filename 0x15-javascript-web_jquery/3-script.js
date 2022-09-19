// Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header
// Info addClass: https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#red_header');
  button.click(function () {
    $('header').addClass('red');
  });
});
