#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');

axios.get(process.argv[2])
  .then(response =>
    fs.writeFileSync(process.argv[3], response.data, 'utf-8')
  )
  .catch(err => console.log(err));
