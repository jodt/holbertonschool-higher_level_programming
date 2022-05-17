#!/usr/bin/node

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films')
  .then(response => {
    const index = (process.argv[2] - 1);
    const film = response.data.results[index];
    for (const character of film.characters) {
      axios.get(character)
        .then(response => console.log(response.data.name));
    }
  });
