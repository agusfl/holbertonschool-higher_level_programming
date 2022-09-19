// Indo JQuery: https://stackoverflow.com/questions/2941679/change-text-color-using-jquery
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#red_header');
  button.click(function () {
    $('header').css('color', '#FF0000');
  });
});
