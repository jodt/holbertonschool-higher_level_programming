#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => {
    const result = {};
    let count;
    let countTemp;
    response.data.forEach(task => {
      if (task.userId in result) {
        count = countTemp;
      } else {
        count = 0;
      }
      if (task.completed) {
        result[task.userId] = ++count;
        countTemp = count;
      }
    });
    console.log(result);
  })
  .catch(err => console.log(err));
