#!/usr/bin/node

'use strict';
let secondMax = 0;

const arr = process.argv.slice(2); // assign arr with the second arg
if (arr.length > 1) {
  arr.sort();
  secondMax = arr[arr.length - 2]; // assign secondMax with the second biggest number in the sorted array
}
console.log(secondMax);
