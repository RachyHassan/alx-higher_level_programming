#!/usr/bin/node
let newArg = 0;

exports.logMe = function (item) {
  console.log(newArg + ': ' + item);
  newArg++;
};
