#!/usr/bin/node
/*
 * A script that computes the number of tasks completed by user id.
 * Requirements
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 * You must use the module request
 */
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const k in tasks) {
      const task = tasks[k];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
