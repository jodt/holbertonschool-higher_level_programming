#!/usr/bin/node

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films')
  .then(async response => {
    const index = (process.argv[2] - 1);
    const film = response.data.results[index];
    for (const character of film.characters) {
      const resp = await axios.get(character);
      console.log(resp.data.name);
    }
  }
  );
