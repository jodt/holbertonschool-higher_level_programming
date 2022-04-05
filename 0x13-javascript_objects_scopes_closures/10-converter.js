#!/usr/bin/node
exports.converter = function (base) {
  return function convertBase (number) {
    return number.toString(base);
  };
};
