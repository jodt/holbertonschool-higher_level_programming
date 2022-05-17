#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
axios.get(url)
  .then(response => {
    let count = 0;
    for (const film of response.data.results) {
      for (const character of film.characters) {
        if (character.includes('18'))
          count++;
      }
    }
    console.log(count);
  }
  )
  .catch(err => console.log(err));
