#!/usr/bin/node

'use strict';

const request = require('request');
const fs = require('fs');
let txt;
request(process.argv[2], function (err, response, body) {
  if (!err) {
    txt = body;
    fs.writeFile(process.argv[3], txt, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
