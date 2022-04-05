#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((x, idx) => x * idx);
console.log(newList);
