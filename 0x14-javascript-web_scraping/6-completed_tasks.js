#!/usr/bin/node

'use strict';

const request = require('request');
const url = process.argv[2];
let a = '';
let list = [];
const dict = {};

request(url, function (err, response, body) {
  if (!err) {
    list = JSON.parse(body);
    for (let i = 0; i < list.length; i++) {
      a = list[i].userId;
      if (list[i].completed === true) {
        if (dict[a]) {
          dict[a] += 1;
        } else {
          dict[a] = 1;
        }
      }
    }
    console.log(dict);
  }
});
