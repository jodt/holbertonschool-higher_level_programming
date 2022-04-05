#!/usr/bin/node
const fs = require('fs');

const firstString = fs.readFileSync(process.argv[2], 'utf-8');
const secondtString = fs.readFileSync(process.argv[3], 'utf-8');

const content = firstString + secondtString;
fs.writeFile(process.argv[4], content, (err) => {
  if (err) {
    console.error(err);
  }
});
