#!/usr/bin/node

const num = process.argv[2];

function fact (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}
console.log(fact(parseInt(num)));
