#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => {
    const result = {};
    response.data.forEach(task => {
      if (task.completed) {
        if (task.userId in result) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
      }
    });
    console.log(result);
  })
  .catch(err => console.log(err));
