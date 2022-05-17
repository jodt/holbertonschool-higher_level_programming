#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios.get(url)
  .then(response => console.log(response.data.title))
  .catch(err => console.log(err));
