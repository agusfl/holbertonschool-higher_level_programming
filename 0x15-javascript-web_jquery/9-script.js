// Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  if (status === 'success') {
    $('#DIV#hello').text(data.hello);
  }
});
