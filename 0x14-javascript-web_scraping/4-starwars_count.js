#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
axios.get(url)
  .then(response => {
    let count = 0;
    for (const film of response.data.results) {
      if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
  )
  .catch(err => console.log(err));
