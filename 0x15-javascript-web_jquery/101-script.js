// Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
// How to remove an element from a list: https://www.geeksforgeeks.org/how-to-remove-contents-of-elements-using-jquery/

// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$(document).ready(function () {
  const buttonAdd = $('DIV#add_item');
  buttonAdd.click(function () {
    $('ul.my_list').append($('<li>Item</li>'));
  });
  const buttonRemove = $('DIV#remove_item');
  buttonRemove.click(function () {
    const items = $('ul.my_list li');
    if (items.length > 0) {
      items[items.length - 1].remove();
    }
  });
  const buttonEmpty = $('DIV#clear_list');
  buttonEmpty.click(function () {
    $('ul.my_list').empty();
  });
});
