#!/usr/bin/node
const arr = [];
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else if (process.argv.length > 3) {
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
