#!/usr/bin/node

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films')
  .then(response => {
    const index = (process.argv[2] - 1);
    const film = response.data.results[index];
    for (const character of film.characters) {
      async function response (character) {
        try {
          const resp = await axios.get(character);
          console.log(resp.data.name);
        } catch (err) {
          console.log(err);
        }
      }
      response(character);
    }
  }
  );
