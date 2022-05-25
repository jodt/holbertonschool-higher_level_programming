$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (titleList) {
  for (const title of titleList.results) {
    $('#list_movies').append(`<li>${title.title}</li>`);
  }
});
