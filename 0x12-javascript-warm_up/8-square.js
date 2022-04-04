#!/usr/bin/node
let str = '';
if (process.argv.length === 2 || !parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    str += 'X';
  }
  for (let j = 0; j < process.argv[2]; j++) {
    console.log(str);
  }
}
