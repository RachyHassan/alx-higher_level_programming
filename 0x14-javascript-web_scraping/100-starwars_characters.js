#!/usr/bin/node
/*
 * A script that prints all characters of a Star Wars movie:
 *
 * Requirements:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 * You must use the Star wars API
 * You must use the module request
 */
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonData = JSON.parse(body);
  const dataChar = jsonData.characters;
  for (const data of dataChar) {
    request.get(data, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
