#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => {
    const result = {};
    let count;
    let countTemp;
    for (const task of response.data) {
      task.userId in result ? count = countTemp : count = 0;
      if (task.completed) {
        result[task.userId] = ++count;
        countTemp = count;
      }
    }
    console.log(result);
  })
  .catch(err => console.log(err));
