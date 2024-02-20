#!/usr/bin/node
// A script that reads and prints the content of a file.
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  if (error) {
    console.log(error || content);
  } else {
    console.log(content);
  }
});
