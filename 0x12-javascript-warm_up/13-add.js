#!/usr/bin/node
// Function that returns the addition of 2 integers.
// Info exports: http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html

const add = function (a, b) {
  return (a + b);
};
exports.add = add;
