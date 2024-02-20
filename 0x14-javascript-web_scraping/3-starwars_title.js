#!/usr/bin/node
/*
 * A script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 *
 * The first argument is the movie ID
 * Star Wars API must use endpoint https://swapi-api.alx-tools.com/api/films/:id
 * use module request
 */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
