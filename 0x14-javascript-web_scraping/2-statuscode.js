#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => console.log(response.status))
  .catch(err => console.log(err.response.status));
