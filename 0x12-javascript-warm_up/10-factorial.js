#!/usr/bin/node
function factorial (number) {
  if (process.argv.length === 2) {
    return 1;
  }
  if (number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(process.argv[2]));
