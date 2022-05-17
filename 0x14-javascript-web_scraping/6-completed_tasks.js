#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => {
    const result = {};
    let count;
    let countTemp = 0;
    response.data.forEach(task => {
      if (task.completed) {
        task.userId in result ? count = countTemp : count = 0;
        result[task.userId] = ++count;
        countTemp = count;
      }
    });
    console.log(result);
  })
  .catch(err => console.log(err));
