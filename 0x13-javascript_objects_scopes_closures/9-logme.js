#!/usr/bin/node
exports.logMe = (function (item) {
  let i = 0;
  return function (item) {
    return console.log(i++ + ': ' + item);
  };
}());
