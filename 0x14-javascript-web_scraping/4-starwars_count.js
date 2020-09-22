#!/usr/bin/node

'use strict';

const request = require('request');
const url = process.argv[2];
let resDict = {};
let count = 0;

request(url, function (err, response, body) {
  if (!err) {
    resDict = JSON.parse(body);
    for (let i = 0; i < resDict.results.length; i++) {
      for (let j = 0; j < resDict.results[i].characters.length; j++) {
        if (resDict.results[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
