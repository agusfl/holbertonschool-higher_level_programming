// Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):
// Info addEventListener: https://www.w3schools.com/js/js_htmldom_eventlistener.asp
// DOMcontentloaded --> https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
